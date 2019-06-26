---
title: "nodenvを使っているとIntelliJ IDEAでnpmのパスが認識されない"
slug: "intellij_with_nodenv"
date: 2019-06-26T22:57:06+09:00
tags:
    - IntelliJ
    - node
---

私はnodeのバージョン管理に[nodenv](https://github.com/nodenv/nodenv)を利用している。しかしなぜかIntelliJ IDEAのNode.js and NPMでnpmのパスが認識されずに困っていた。

環境変数の問題かといろいろ設定を見直したりしていたが、別にそこまでnodeを使うわけでもないので、まあいいかと放置していた。が、今日調べてみたらそれを解決するツールがあったので紹介しておく。

<!--more-->

## jetbrains-npm

単にこれを導入すればオッケーというだけの話で終わってしまうのだけれど。

<https://github.com/nodenv/jetbrains-npm>

私はnodenvをデフォルトの設定でインストールしているので、[jetbrains-aware git clone](https://github.com/nodenv/jetbrains-npm)の手順に従ってインストールした。結果、無事にIntelliJ IDEAにnpmのパスが認識されるようになった。

スターがあまりついていないので、あまり知られていないのか、それともそもそも困っている人が少ないのか。まあnodeやるならVSCodeでいい気はするからね・・・。

ともかく、私のようにnodenv + IntelliJ IDEA(もしくはWebStorm)を使っていてnpmのパスが認識されなくて困っている人の助けになれば幸いである。