---
title: "Visual Studio Code＋Vimプラグインでctrl-[のキーバインディングを変更する"
slug: "customize_keymapping_vim"
date: 2016-09-12T19:30:00+09:00
tags:
    - VSCode
    - 設定
    - vim
---

VSCodeとVimプラグインを利用していて、キーマップの違いによる問題に遭遇したので紹介しておく。

ちなみにこれはMac+JIS配列キー特有の問題なのかもしれない。

<!--more-->

私はVimではないIDE（Android Studioとか）でもVimプラグインなどを利用して、Vimスタイルでコードを書くようにしている。それぞれのIDEやエディタ特有のキーバインドを覚えるのが面倒くさいからだ。

何より一行下に新しくコードを書くのにノーマルモードでoを押すだけでいいのが便利でいい。そういう機能はIDEやエディタ側で用意されているのだろうけれども、それぞれのエディタごとで覚えるのが面倒くさい、ただそれだけなのである。

決して私がヘビーVimmerというわけではない。簡単なのしか使ってないから、別にVimでなくてもいいといえばそれまで。

で、Vimでインサートモードから抜けるのにESCキーを使うが、私はCtrl-[を使っている。もう長いことこれを使うスタイルなので、癖になっている。

ちなみにこれがJIS配列のキーを使っていると、Vimプラグイン上で問題になることが多い。実際に多いのかどうかは知らないが、例えばAndroid Studio（IntelliJ系IDE）では問題になる。JIS配列のキーボードでは、キートップに`[`と刻印してあるキーは、内部で`]`として扱われてしまうことがある。

これはVimプラグインではなくIDEの問題なのだけれどしょうがない。私はAndroid StudioではVimプラグインの設定ファイル（.ideavimrc）でキーバインドを変更することで対処している。

で、Visual Studio Codeでも同じ問題にぶち当たった。VSCodeよお前もかという感じである。

VSCodeでは.vimrcみたいな設定ファイルで設定を行うわけではない。設定用jsonファイルをいじることになる。基本設定のユーザー設定を開きsettings.jsonに設定する。

```
"vim.insertModeKeyBindings": [
        {
        "before":["ctrl+]"],
        "after":["&lt;Esc&gt;"]
        }
    ]
```

とするといいはずなのだが、この設定は無視される。どうもプラグイン側で`ctrl+[`が認識できないらしい。ctrlといった修飾キーが認識できないのか、それとも`]`などの記号がダメなのかはちょっと良くわからない（英語力がないのが悩ましい）。

`"vim.useCtrlKeys": true`

とすれば、`ctrl+[`でEscできるが、VSCode＋Mac＋JISキー配列だとこれは`ctrl+@`になってしまう。VSCodeだけ＠にするというのは非常にストレスなのでなんとかしたい。

とりあえずはVimプラグインではなく、VSCodeのキーボードショートカットで対処することにした（対処できた）。

```
[{
    "key": "ctrl+]",
    "command": "extension.vim_escape",
    "when": "editorTextFocus"
}]
```

issueはここ<a href="https://github.com/VSCodeVim/Vim/issues/757">https://github.com/VSCodeVim/Vim/issues/757</a>