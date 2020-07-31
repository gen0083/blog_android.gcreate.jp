---
title: "Fragmentで初期化処理を行うのはどこでやるのか"
slug: "fragment_onviewcreated"
date: 2020-07-31T23:41:47+09:00
tags:
    - Android
    - Fragment
---

Fragmentでの初期化処理を行う場所どこだっけとなったので備忘録として残しておく。

処理する場所が変わったんだな、ということだけは記憶にあったのだが、結局どこになったのだったかなと迷ってしまった。この先何回も遭遇しそうだったので、ブログに残しておこうと思う。

<!--more-->

## onActivityCreatedはdeprecatedに

androidx.fragmentのバージョン1.3.0からonActivityCreatedがdeprecatedになる。

<https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha02>

これまではActivityの初期化処理が終わった後にFragmentで行う処理の初期化を行う、としていた。

しかしViewにFragmentでViewに依存する処理は`onViewCreated`で、そもそもViewに依存しない処理なら`onCreated`で初期化を行えばよい。

まだalphaだから切り替わっていないが、今後は`onViewCreated`でViewにまつわる処理の初期化はすればよい。

これまでFragmentの初期化は`onActivityCreated`をずっと使っていたので、しばらく迷いそうである。ただ、正式にdeprecatedになったらAndroid Studioで警告が出るようになるだろうから特に心配しなくてもよいかもしれない。