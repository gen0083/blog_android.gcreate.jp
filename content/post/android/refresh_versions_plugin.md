---
title: "ライブラリのバージョン管理をしやすくするrefreshVersionsを試してみた"
slug: "refresh_versions_plugin"
date: 2021-06-19T16:23:13+09:00
tags:
    - "Android Studio"
    - Gradle
---

Gradleでライブラリの管理を便利にできそうなプラグインを見かけた。refreshVersionsというプラグインだ。

buildSrcを使って一括管理する方法は知っていたが、プロジェクトごとに用意するのも面倒くさい。なにか楽な方法はないかと思っていたが、これはその解の1つとなりそう。

<!--more-->

## 導入してみた感想

[GitHub](https://github.com/jmfayard/refreshVersions)

[ドキュメント](https://jmfayard.github.io/refreshVersions/)

Gradleプロジェクトで各モジュールが依存しているライブラリを`dependencies`ブロックで記述する。これがシングルモジュールであれば問題はないだろうが、マルチモジュール構成になるとバージョン管理が大変になる。このrefreshVersionsプラグインはそれを解決するためのものだ。

導入すると依存するライブラリのバージョンが`versions.property`ファイルにまとめられる。

さらに使えるバージョンの候補、というよりは指定しているバージョンよりも新しいものがあれば、バージョンアップ候補としてコメントアウトされた状態で追加される。

```
version.androidx.appcompat=1.3.0
##             # available=1.4.0-alpha01
##             # available=1.4.0-alpha02
```

これは`./gradlew refreshVersions`を実行すれば再チェックされる。

ライブラリの指定方法も、refreshVersions側でよく使われるものが定義されている。たとえば`AndroidX.appCompat`のように依存ライブラリを追加できる。これも便利。

例としてCoroutinesを追加したいとしよう。これまではアーティファクト名がわからず毎回ネットで公式サイトを調べる必要があった。これをrefreshVersionsを使うと`KotlinX.coroutines.android`とするだけですむ。

これはKotlin DSL（build.gradle.kts）を使っているとコード補完で参照できる。素のGroovyの状態でも参照できる(`implementation KotlinX.coroutines.android`とすればよい)。しかしコード補完が効かないので利便性は少し落ちる。

ただしKotlin DSLを使うと現時点では素のgroovyの状態と比較するとコード補完の候補が出るまで時間がかかる。レスポンスに問題が出てくるのでどちらでいくかは悩ましいところ。

## バージョンの指定

refreshVersionsに登録されていないライブラリに対しても、バージョンチェックの機能をrefreshVersionsに委譲できる。やり方はかんたんでライブラリのバージョン部分を`_`に置き換えるだけだ（たとえば`com.example.hoge:hoge:1.0.0`を`com.example.hoge:hoge:_`にする）。

refreshVersionsが`_`で指定されているバージョン部分を、versions.propertyを参照して解決してくれる。

これはルートのbuild.gradleファイルに記述するbuildScriptの部分にも適用される。

KotlinのGradleプラグインを導入するのに、buildscript内にKotlinのバージョンを定義してプロジェクト内で参照する方法をよく使っていた。これもrefreshVersionsで管理できる。

```
buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath("com.android.tools.build:gradle:_")
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:_")
    }
}
```

buildscript内は特殊というイメージがあったので、ここも含めて一元管理できるのは便利でいいなと思った。

## 導入にあたってハマったこと

`Cannot get version candidates with an empty fetchers list.`というエラーメッセージが出てライブラリのバージョンが解決できなかった。

原因はルートのbuild.gradleファイルで各プロジェクトに使うリポジトリを定義していなかったことのようだ。

ルートbuild.gradleで`allprojects`（もしくは`subprojects`）でリポジトリを明示的に指定すれば取得できるようになった。

もちろんapp/build.gradle等の各モジュールで個別に指定してもよいが、マルチモジュール環境で使うことを考えたらルートで指定するほうがよい気がする。
