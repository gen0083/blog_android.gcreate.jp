---
title: "OkHttpを使ってAndroidでネットワークリクエストを行う"
slug: "network_request_with_okhttp"
date: 2020-02-08T20:33:43+09:00
tags:
    - Android
    - Kotlin
    - coroutine
    - OkHttp
---

Android端末でネットワークリクエストを行う方法について書いてみる。APIを叩く＝Retrofitを使うという図式があるのだが、まずその前段階としてOkHttpを使ってネットワークリクエストをしてみようと思う。

Androidでネットワークアクセスする記事ってあんまりないかもって思ったので書いてみることにした。ついでにいうとリハビリを兼ねてというのと、自分でも振り返ってみるとどうやるんだっけってなったのがきっかけである。

<!--more-->

## 注意事項

ネットワークリクエストを行う前に、Androidにおける作法として、インターネットアクセスを行う際にはパーミッションの追加が必要である。パーミッションの追加は熟練者であろうとも結構忘れる。ログを見るとパーミッションがないぞというエラーが出るのですぐに分かるのだが、サンプルアプリを作ったりする際によく忘れる。

もう1つやりがちなのが、メインスレッドでネットワークリクエストを行うと例外なくアプリが落ちる。必ずワーカースレッドなりでメインスレッドをブロックしない形でネットワークリクエストを行う必要がある。これもログを見ればすぐに分かるエラーである。

- スレッドを別に立ててネットワークリクエストを行う
- AsyncTaskを使う
- RxJavaを使ってスレッドをスイッチする
- Kotlinのcoroutineを使う
- OkHttpのenqueueメソッドを使う

など、いろいろな方法があるが、メインスレッドでネットワークリクエストを行ってはならないということだけは覚えておく必要がある。

理由としては、メインスレッドで通信を許可してしまうと、結果が帰ってくるまでの間UIの更新が一切できないからである。「ネットワークリクエスト中はUIの更新しないからいいし」と思うかもしれないが、更新のみではなく操作も受け付けなくなってしまうのでダメなのである[^1]。

この2つは前提として理解しておきたい。

## 準備

まずは最初に書いたパーミッションの追加である。

AndroidManifest.xmlに`<uses-permission android:name="android.permission.INTERNET" />`を追加する。これは`<application>`タグの前に書く。

次はOkHttpを使うための準備である。

<https://square.github.io/okhttp/>

app/build.gradleに`implementation "com.squareup.okhttp3:okhttp:4.3.1"`を追加することで導入できる。

今回はついでなのでKotlinのcoroutineを使うのも併用してみようと思う。coroutineのセットアップも同様にapp/build.gradleにライブラリの依存情報を追加することで導入できる。

<https://github.com/Kotlin/kotlinx.coroutines>

```
    def coroutines_version = "1.3.3"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-core:$coroutines_version"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:$coroutines_version"
```

バージョンは適宜最新のものを使ってほしい。

ついでにDataBindingも有効にしておく。Viewへのアクセスが楽になるから[^2]という理由で私はいつもこれを使うのだが、使わない人はViewへのアクセス部分を適宜読み替えてほしい。

<https://developer.android.com/topic/libraries/data-binding/start.html>

```
dataBinding {
    enabled = true
}
```

## コード

activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<layout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    >

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity"
        >

        <ScrollView
            android:id="@+id/scrollView2"
            android:layout_width="0dp"
            android:layout_height="0dp"
            app:layout_constraintBottom_toTopOf="@+id/get_html"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintHorizontal_bias="0.5"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent"
            >

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical"
                >

                <TextView
                    android:id="@+id/textView"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Hello World!"
                    />
            </LinearLayout>
        </ScrollView>

        <Button
            android:id="@+id/get_html"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="get html"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toStartOf="@+id/get_api"
            app:layout_constraintHorizontal_bias="0.5"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/scrollView2"
            />

        <Button
            android:id="@+id/get_api"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="get api"
            app:layout_constraintBottom_toBottomOf="@+id/get_html"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintHorizontal_bias="0.5"
            app:layout_constraintStart_toEndOf="@+id/get_html"
            app:layout_constraintTop_toTopOf="@+id/get_html"
            />

        <androidx.core.widget.ContentLoadingProgressBar
            android:id="@+id/progress_bar"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent"
            />

    </androidx.constraintlayout.widget.ConstraintLayout>
</layout>
```

MainActivity.kt

```
package jp.gcreate.sample.networksample

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import jp.gcreate.sample.networksample.databinding.ActivityMainBinding
import kotlinx.coroutines.*
import okhttp3.*
import java.io.IOException

class MainActivity : AppCompatActivity(), CoroutineScope by MainScope() {

    private lateinit var binding: ActivityMainBinding
    private val okHttpClient = OkHttpClient.Builder().build()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)

        binding.getHtml.setOnClickListener {
            launch {
                binding.progressBar.show()
                val request = Request.Builder()
                    .url("https://android.gcreate.jp/")
                    .build()
                val result = withContext(Dispatchers.IO) {
                    okHttpClient.newCall(request).execute().use { response ->
                        if (response.isSuccessful) {
                            response.body?.string()
                        } else {
                            "failed/ code: ${response.code} / message: ${response.message}"
                        }
                    }
                }
                binding.textView.text = result
                binding.progressBar.hide()
            }
        }

        binding.getApi.setOnClickListener {
            binding.progressBar.show()
            val request = Request.Builder()
                .url("https://jsonplaceholder.typicode.com/todos/1")
                .build()
            okHttpClient.newCall(request).enqueue(object : Callback {
                override fun onFailure(call: Call, e: IOException) {
                    runOnUiThread {
                        binding.textView.text = "error: $e"
                        binding.progressBar.hide()
                    }
                }

                override fun onResponse(call: Call, response: Response) {
                    val result = if (response.isSuccessful) {
                        response.body?.string()
                    } else {
                        "failed/ code: ${response.code} / message: ${response.message}"
                    }
                    runOnUiThread {
                        binding.textView.text = result
                        binding.progressBar.hide()
                    }
                }

            })
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        cancel()
    }
}
```

コード全体はGitHubにアップしてある。

<https://github.com/gen0083/NetworkSample>

## 解説

今回はgetHtmlとgetApiの2つを用意した。

getHtmlの方はcoroutineを使いOkHttpの`execute()`による同期呼び出しによるネットワークアクセスを行っている。一方でgetApiの方はOkHttpの`enqueue()`を使い非同期ネットワークアクセスを行っている。

両者の違いは、ネットワークリクエストを呼び出すのがメインスレッドでも大丈夫かどうかの違いである。

`execute()`は結果が帰ってくるまでその部分で処理を待つので、実行スレッドをブロックする。そのためメインスレッドでこれを呼び出すことはできない。そのため今回のコードではcoroutineを使い別スレッドで実行している（`withContext(Dispatchers.IO) {}`の部分）。

一方で`enqueue()`は実行スレッドをブロックしない。代わりに`enqueue()`の引数で指定する`Callback`内にネットワークアクセスを行った結果が通知される。そのためメインスレッドで呼び出しても問題がない。

OkHttpの使い方は、基本的には`Requset`を作成して、`OkHttpClient`に渡して`execute()/enqueue()`を行うことでネットワークアクセスを行う。`OkHttpClient`はアプリケーション内でシングルトンにすることが多いと思われる[^3]。今回はそこまでやってないけれど。

## coroutineの起動

`Activity`でcoroutineを起動するには`Activity`に`CoroutineScope by MainScope()`を実装すればよいようだ。

ちなみに`Activity`でcoroutineを起動するのは実際にはあんまりないような気もする。`ViewModel`で行うほうが一般的だと思われるが、今回は単純なサンプルなので`Activity`で起動している。

他に`GlobalScope.launch{}`で起動する手もあるけれど、[kotlinx.coroutinesのサンプル](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/)に従った方法を使ってみた。`GlobalScope`を使うのはライフサイクルを考えると避けたほうがいいという話があるので。

## 余談

ネットワークリクエストはメインスレッドで行ってはならない。一方でUIを更新する処理、今回のサンプルで言えば`binding.textView.text = "..."`としている部分については、メインスレッドでなければ実行できない。UIを触る処理は逆にメインスレッド以外から行ってはならないのである。ややこしい。

そのためcoroutineを使っている部分に関しては、ネットワークアクセスを行う部分のみ`withContext(Dispatchers.IO)`でIOスレッドで実行するようにしている。特に`Dispatchers`を指定せずに`launch`すると、今回は`MainScope()`を使っているので`launch{}`内のコードはメインスレッドで呼び出しが行われる。

一方で`enqueue()`を使っている方ではViewの更新を行う部分は`runOnUiThread {}`経由で行っている。これはコールバック内はワーカースレッドから呼び出されているので、ここで直接Viewを触るとエラーで落ちるからである。

個人的にはcoroutineを使った同期処理のほうがコードが読みやすくて分かりやすいと思う。ただ、`withContext()`の部分がそのままでは分かりづらい書き方になっているのが気にはなる。

`withContext()`は指定したコンテキスト、この例で言えばIOスレッドを使ってブロック内の処理を行う。そしてそのブロック内の処理結果を返すものになっている。結果手的に、とってきたHTML、もしくはエラーがおこればその内容の文字列がresultとして返ってくるという処理になる。しかしもうちょっと読みやすくできそうな気はする。

[^1]: メインスレッドをブロックするということは、画面が固まるだけでなく操作イベントも処理できなくなってしまう。これはネットワークリクエストに限らず、メインスレッドで重い処理をしてはならないのだが、その中でも特別にネットワークリクエストに関してはOS側が検知してアプリを強制的に終了させる仕組みがある。
[^2]: `findViewById()`が省略できるので。
[^3]: DaggerなどのDIライブラリを利用して、アプリケーション内でシングルトンになるようにするのがセオリーだろうか。