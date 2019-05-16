---
title: "Android StudioでJDKのパスを指定する"
slug: 129
date: 2014-10-26
lastmod: 2014-10-26
tags: 
---

久しぶりにAndroid Studioでサンプルアプリを作ろうとしたら、JDK7を使えと怒られてしまいました。

設定を確認すると、JDK6を使うように設定されていました。

![Project Structure](Project-Structure.jpg)

Project Structureは`cmd + ;`で開きます。

JDKは1.8をインストールしていたはず・・・と思って確認すると、やっぱり1.8がインストールされていました。

![コマンドプロンプトでJDKのバージョン確認](648dc5e33bc2e6dc857c3bed93b9d203.jpg)

コマンドプロンプトを開いて`java -version`でインストールされているJavaのバージョンが確認できます。（正確にはJREのバージョンの確認ですけど）

しかし、`/System/Library/Java/JavaVirtualMachines`にはJDK6しかない。調べてみると、JDK1.7以降ではインストールされているディレクトリが異なる模様。

それぞれのJDKのディレクトリを確認するには、コマンドプロンプトで`/usr/libexec/java_home -v バージョン`で、JDKのバージョンごとのインストールされているディレクトリが確認できます。

![java_homeコマンドでインストールされているディレクトリを確認](487a50ab14c805ecc7a483f949ad1ce9.jpg)

とりあえずJDK7を使えというエラーメッセージだったので、JDK7のディレクトリを指定してやることでエラーメッセージが消えました。

![JDK7を使えというエラーメッセージ](78e492b39af42453b37a588220b6bfa0.jpg)

ちなみに、JDK7は<a href="http://www.oracle.com/technetwork/jp/java/javase/downloads/jdk7-downloads-1880260.html">Oracleのサイト</a>からダウンロードできます。


  