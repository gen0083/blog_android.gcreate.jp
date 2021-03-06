---
title: "Adaptive Icon"
slug: 421
date: 2018-01-12
lastmod: 2018-01-12
tags:
    - Android
    - UI
---

Adaptive IconをFigmaを使って作ってみた。

![Adaptive icon](adaptive_icon.jpg)

Adaptive Iconは、開発者側はアプリのアイコンとなる前景画像と背景画像の2種類だけを用意して、後のアイコンの形はOS（デバイス側）にまかせてしまうという仕組み（という理解を私はしている）。

今まではランチャーアイコンとして四角いやつと丸いやつの2種類を別途用意していたけども、これからは2種類の画像（前景と背景）さえ用意しとけば後はOS側（正確にはホームアプリ？）がアイコンの形をよしなに表示してくれる。

といってもAPI26からの機能なので、現実的には依然として普通のランチャーアイコンは用意しなければならない。

とはいえ今回Figmaを使ってアイコンを作ってみたが、25以下のための画像データを用意するのはそこまで手間だとは感じなかった。108dpでアイコンデータを作っているので、その画像をAndroid Asset Studioに持っていってランチャーアイコンを生成するだけだったので。


## Figmaを使ってアイコンデータ作成


今回は<a href="https://www.figma.com/">Figma</a>を使ってアイコンデータを作成した。ちなみにベクターデータである。

作成したforeground画像とbackground画像を、Adaptive Iconとして表示した場合にどうなるかは、<a href="https://adapticon.tooo.io/">このツール</a>を使ってシュミレーションしながら確認した。

Adaptive Icon非対応の端末用の既存のランチャーアイコンは、Figmaから書き出した画像データを<a href="https://romannurik.github.io/AndroidAssetStudio/index.html">Android Asset Studio</a>を使って生成した。

こんな感じで作成。

![Icons](icons.jpg)

これは重ね合わせた状態だが、前景と背景別々に作ってある。

![Fore back](fore_back.jpg)

どちらの画像も108dp四方になるように、108dpの矩形を別途用意した上で、その上にアイコン要素を描画するようにしている。そうしないとエクスポートした際に108dpの画像として出力できないからである。

作成した画像はforegroundとbackgroundそれぞれをSVGでエクスポートして、そのSVGファイルをVector Drawableに変換してAndroid Studioへ持っていった。

Vector Drawableへの変換は<a href="https://a-student.github.io/SvgToVectorDrawableConverter.Web/">このツール</a>を利用した。

複雑な形状だとうまく変換できないこともあるので、適宜調整が必要だろう。Vector Drawableとしてうまく変換できたとしても、パスデータが複雑すぎるという警告が出ることもある。あまり複雑すぎるのも考えものである。

ちなみにFigma用のAdaptive Iconのテンプレートがあったので、<a href="https://medium.com/google-design/designing-adaptive-icons-515af294c783">こちら</a>
から利用させていただいた。

テンプレートのサイズはFigma上では432になっている。Adaptive Iconは108dpで作成するものだ。FigmaとかSVGの仕様とかに疎いのでよくわからないのだが、432のサイズでアイコンを作成してSVGでエクスポートしても問題ないのだろうか？

私はよくわからなかったので、アイコンサイズを108の大きさで作成した。

ちなみに432とか単位をつけずに書いているのは、Figma上での単位が分からなかったからである。432のままSVGエクスポートしてVector Drawableに変換すると432dpになってしまい、そこからXMLの数値を108dpに書き換えるだけで問題ないのかよくわからなかったので、最初からFigmaの段階で108のサイズで作成したというわけ。

ちなみにテンプレートは一旦フラット化してベクター情報に変換し、サイズを108に縮小してアイコン画像の位置調整のガイドとして利用させてもらった。


## Adaptive Iconの対応状況


こうして作成したAdaptive Iconだが、これが表示できるかどうか使っているランチャー次第のようだ。

私の場合、実機Nexus6P（Android 8.1.0）に作ったAdaptive Iconのアプリをインストールしても、固定されたアイコンとしては表示されるものの、アニメーション（ぷるぷる動くような視覚効果）はしなかった。

Pixel Launcherだとぷるぷるするらしい。

<blockquote class="twitter-tweet" data-lang="ja">
<p lang="ja" dir="ltr">Pixel2のLauncherでアイコン長押ししてふったりすると動いたりします

&mdash; takahirom (@new_runnable) <a href="https://twitter.com/new_runnable/status/951705339790938113?ref_src=twsrc%5Etfw">2018年1月12日</a>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

私の使っているランチャーはGoogle Nowランチャーなので、Adaptive Iconにきちんと対応しているわけではないようだ。アイコンとして表示することはできるが、アイコンのシェイプを変えたり、アニメーションしたりしない。

試しに他のランチャーをインストールして試してみたところ、Adaptive Iconへの対応を謳っているランチャーであればAdaptive Iconがぷるぷるすることを確認した（私が試したのはNova Launcher）。


## 参考


<a href="https://qiita.com/takahirom/items/696fb5ecaa230fa8f755">3分で分かる？Android OのAdaptive Iconに対応しよう</a>

<a href="https://adapticon.tooo.io/">Adaptive Iconのシミュレーションツール（Web）</a>

<a href="https://medium.com/google-design/designing-adaptive-icons-515af294c783">Designing Adaptive Icons（各ツールにおけるテンプレートへのリンクあり）</a>

<a href="https://a-student.github.io/SvgToVectorDrawableConverter.Web/">SvgToVectorDrawableConverter.Web（SVGをVector Drawableに変換するツール）</a>


  