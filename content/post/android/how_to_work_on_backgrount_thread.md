---
title: "Androidで非同期処理を行う方法"
slug: "how_to_work_on_backgrount_thread"
date: 2020-02-27T00:21:53+09:00
tags:
    - Android
    - 非同期処理
    - RxJava
    - coroutine
---

Androidでネットワークアクセスするときにはメインスレッドで実行できないという話を書いた。今回はその続きで、どうやってメインスレッド以外で処理するかという話を書きたい。

<!--more-->

## 選択肢

[前の記事]({{< ref "network_request_with_okhttp" >}})では、いろいろ考えられる方法を書いた。しかし実質的には、RxJavaを使うかcoroutineを使うかのどちらかが選ばれるだろう。

JavaのThreadめっちゃ詳しくて使いこなすの余裕ですっていう人は、自前でThread処理すればいいと思うが、私にはハードルが高すぎるのでライブラリを使う。coroutineが出るまでは、非同期処理のためだけにRxJavaを使うくらいの気持ちだった。今はcoroutineを使う方が多い。

AsyncTaskをAndroid開発で使うことはほぼないと思っていい。公式ドキュメントには相変わらずAsyncTaskが書かれているけれど、もうこれDeprecatedにすべきでは思う。と思ったがついにAndroid 11からDeprecatedになった。正式に使うべきではなくなった。

AsyncTaskを使わない理由は、Activityと密結合しすぎるからだと思っている。非同期処理を行った結果はUIに表示することが多いだろうから、そのときにAsyncTaskがUIを更新するような書き方をしなければならなくなる。もっとも、そもそもAsyncTaskがぱっとみわかりにくいから使いたくないというのが正直なところ。

## 非同期処理のイメージ

Threadを使うのもRxJavaやcoroutineを使うのも、どれも通常の同期的な処理から、非同期処理ワールドを作って処理の流れを分岐させるイメージで私は捉えている。

通常であれば関数を呼び出せば、その関数の処理が終わってからはじめて次の行に処理が移動する。しかし非同期処理ワールドに分岐すれば、即座に次の行の処理に移動する。処理の流れがそこで分岐するからである。

## RxJava

RxJavaでは`subscribeOn()`や`observeOn()`を使うことで実行スレッドの切り替えが容易にできる。この仕組みを利用して非同期処理はワーカースレッドにスイッチするのである。

ただ非同期処理のためだけにRxJavaを導入するのは手段と目的を履き違えている気がするし、なによりReactive Streamの学習コストがかなり高い。しかしReactive Streamの概念はRxJavaのみならず、いろいろなところで利用されている[^1]ので学習しておいて損はない。

Streamを扱うついでに非同期処理もいい感じに処理できるのは利点である。


## Coroutine

CoroutineScopeからlaunchすることでCoroutineが起動する。

CoroutineScopeがまたわかりにくいかもしれない。というか私もわかってるようでわかってない。とりあえずCoroutineの世界を起動するためにはCoroutineScopeが必要という程度の認識だ。

非同期処理を行っているのにコードの見た目は同期的なのがよいところ。コードの可読性は良いと思う。


## 今回のサンプル

1. 非同期処理に入る前にTextViewを更新
2. ワーカースレッド（もしくはCoroutine）でAPIを呼び出す
3. APIの結果をTextViewに設定

という処理を行う。

まずはRxJavaだと次のような感じになる。

```
Single.fromCallable { callApi() }
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .doOnSubscribe {
                    binding.textView.text = "work with RxJava"
                }
                .subscribe({
                    binding.textView.text = "with RxJava: $it"
                }, {
                    binding.textView.text = "onError RxJava: $it"
                })
```

私の捉え方は次のような感じである。

`subscribe`でイベントの結果が流れてきたときの処理を登録する。`subscribe`をトリガーにStremaの処理の流れを下からさかのぼっていく。今回は`doOnSubscribe`があるのでその処理がまず走る。さらに上にさかのぼって`subscribeOn`で実行スレッドがスイッチされる。そしてようやく`callApi()`が呼び出され、その結果が`subscribe`に向かって流れていく。`observeOn`があるので、そこでメインスレッドに処理の流れがスイッチし、最終的に`subscribe`の中に`callApi()`の結果が到達する。

`subscribe`することでStreamの根本まで`subscribe`されたことが伝わっていき、根本まで伝わったらそこからStreamが流れていく、というイメージを持っている。[^2]

一方同じことをCoroutineでやるとこうなる。

```
           launch {
                binding.textView.text = "work with Coroutine"
                val result = withContext(Dispatchers.IO) { callApi() }
                binding.textView.text = "with Coroutine: $result"
            }
```

処理を実行する前にTextViewを更新し、IOスレッド（といっていいのかはよくわからないが）で`callApi()`を呼び出し、その結果をTextViewにセットして終了。`withContext`の部分がいまいち分かりづらい気がするけれど、非常に直感的な書き方になっている。

`launch`内は特に何も指定していないので、ここに書いている処理はメインスレッドで呼び出されることになる。

`withContext`で`Dispatcher`を設定している部分だけがワーカースレッドで動いている。その処理結果が帰ってきてから最後のTextViewの更新が行われるわけだが、Coroutineワールドでは実行スレッドをブロックしない。そのためこの処理待ち時間の間でもUI更新に影響を与えることはない。

今回のコードは[ここ](https://github.com/gen0083/NetworkSample/blob/master/app/src/main/java/jp/gcreate/sample/networksample/BackgroundWorkFragment.kt)


[^1]: JetpackのLiveDataを理解するのにも役に立つ。
[^2]: 余談だが、私はReactive Streamを流しそうめんで認識している。Operatorを使ってイベントを連結するのは、流しそうめんが流れる竹を連結している作業で、subscribeするのは流しそうめんを食べる人が下流に来たという状態。食べる人が来たらそうめんを流し始めるというようなイメージである。