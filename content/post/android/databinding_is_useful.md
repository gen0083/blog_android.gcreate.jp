---
title: "DataBindingは便利"
slug: "databinding_is_useful"
date: 2016-06-09T15:31:06+09:00
tags:
    - Android
    - DataBinding
    - ポエム
---

Androidアプリを書くのに、最近私はいっさいfindViewByIdを書かない。簡単なサンプルでも必ずDataBindingを使って書いている。

<!--more-->

以前はButterKnifeを使っていたのだけれど、DataBindingを使ってみたらとても手軽で便利だったので、すっかり移行してしまった。ButterKnifeがXMLのIDをJavaのコード側に持ってくるイメージとしたら、DataBindingはXMLにJavaのコードを持っていく感じになる。

DataBindingを使えば「表示にこのクラスを使ってくれ」と渡すだけで、Javaのコード上からTextView.setText()とかしなくてすむようになるのだ。ActivityからViewを更新するためのコードが消え去るので、非常にすっきりしてよい。

サンプルコードを写経するときには、わざわざViewを触る部分についてはDataBindingで書いてしまう（写経になってないけど）程度にはDataBinding大好きマンになってしまった。