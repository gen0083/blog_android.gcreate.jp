---
title: "Android Support LibraryのソースコードをGrepCodeを使って確認する"
slug: 168
date: 2014-12-20
lastmod: 2014-12-20
tags:
    - Android
---

Android Support LibraryのソースコードはAndroid Studioで確認することができません

例えば、android.support.v7.app.ActionBarActivityのソースコードを確認したいとしましょう。その場合、調べたいクラスをCmd+クリックすることで、対象のクラスのソースコードに自動的にジャンプできます。

![Android Studioでソースコードを確認する](6eb11c616704a61f7fabe63eae153a67.jpg)

しかし、サポートライブラリについてはソースコードまでは見つかりません。

![ActionBarActivity](ActionBarActivity.jpg)

ちなみにAndroid SDKのクラスであれば、SDKマネージャーでソースコードまでダウンロードしていれば確認することができます。例えばBundleクラスのソースコードは以下のように確認できます。

![例：Bundleのソースコード](0fd4ce27d24a1d0c8359e43ff8d58e9b.jpg)

サポートライブラリのソースコードを確認するのは、Gitを使ってGoogleのリポジトリから拾ってくる方法もありますが、今回はWebサービスのGrepCodeを利用してみます。

<a href="http://grepcode.com/" class="broken_link">GrepCode</a>にアクセスして、検索したいクラスを入力します。（今回の場合はandroid.support.v7.app.ActionBarActivity）

![検索したいクラスを入力](cb0c23581f939230a15e58d59babe95f.jpg)

すると検索結果が表示されるので、調べたいクラスのバージョンを選択します。

![バージョンを選択](d30bc00ee8753b6de9a0866202a57b90.jpg)

他のバージョンとの差異をDiffで確認できるので、バージョンアップでどこが変更されたのかを調べるのにはちょうどいいかもしれません。

![他バージョンとの際はDiffで確認できる](5540faa9733549b0f604fb3995f2449b.jpg)

![比較するバージョンを選択](838451857577d15c1822e7a0078349cf.jpg)


  