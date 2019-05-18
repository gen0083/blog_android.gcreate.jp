---
title: "Android Studio 1.0正式版がリリースされています"
slug: 154
date: 2014-12-09
lastmod: 2014-12-09
tags:
    - "Android Studio"
---

Android Studio 1.0が正式版になりました。

<a href="http://tools.android.com/recent/androidstudio10released">Android Tools Project Site > Recent Changes</a>

<a href="http://android-developers.blogspot.jp/2014/12/android-studio-10.html">Android Developers Blog > Android Studio 1.0</a>

プレビューバージョンで暫定的に取り込まれていた機能が洗練されたり、正式版になって新たにサポートされるようになった機能があったりします。


## ウィザードからサンプルコードを取り込めるようになった


個人的にはウィザードからAndroidのサンプルコードを取り込むことができるようになったのが気になるところです。

![Android Studio 1.0　ウィザードからサンプルコード取り込み](a357c56cc6f92259065fd65105413a0f.jpg)

こういう機能を実装するにはどうすればいいのかというサンプルがいろいろと用意されているようです。画面のあるものについては、プレビュー画面で画像が表示される仕組みになっていました。（サンプルコードがGitHubで公開されていて、そこに画像があれば表示するってだけですけど）

![Android Studio 1.0 サンプルコード](a85f32cf08acd94b22ae07a53f1d0300.jpg)

サンプルコードをウィザードで取り込めると、変なところでハマったりしなくて済んで楽チンですね。


## 画面レイアウトのプレビューがパワーアップ


Layout.xmlをいじる際の画面プレビューが進化してます。

画面サイズごと、Androidのバージョンごとのプレビューを一覧表示できるようになってます。表示がおかしくならないかチェックするのに便利です。

![Android Studio 1.0 画面プレビュー](ce418dabcc8f7f3ac4df42458ad2ac2a.jpg)

![Android Studio 1.0 スクリーンサイズごとの一覧](ffc2a40f0ae0c83f327439028435bbc6.jpg)

![Android Studio 1.0 OSバージョンごとの一覧](e87c9729bf5d8426492f1c182594b6f8.jpg)


## 以前のバージョンで作ったプロジェクトを開くとき


runProguard　→　minifyEnabledに名前が変わっています。自動的に直してくれてよさそうなものですが、私のケースでは直してくれませんでした。

他にもGradleプラグインの更新によって、うまいことプロジェクトが開けない場合があると思います。

SSとるために開いた限りではこの&#8217;runProguard&#8217;が引っかかったので、以前のAndroid Studioを使って作ったプロジェクトを開く際に覚えておくといいと思います。

詳しいところは<a href="http://tools.android.com/tech-docs/new-build-system/migrating-to-1-0-0">Migrating Gradle Projects to version 1.0.0</a>を参照するといいと思います。


  