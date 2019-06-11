---
title: "VSCodeのVimプラグインでUndo/Redoの設定を調整する"
slug: "vim-undo-redo"
date: 2019-06-11T19:52:53+09:00
tags:
    - VSCode
    - 設定
---

私はVSCodeでVimプラグインを使っている。VSCodeのVimを使っていて微妙に困るのが、Vim経由でUndoをすると、自分の想定しているものより多くの変更がもとに戻ってしまうことだ。

この問題は開発元でもIssueとして認識されているが、今のところ解決には至っていない。そこで今回は、この問題の現時点(2019年6月)での回避策を紹介したい。

<!--more-->

## VimのUndoがダメならVSCodeのUndoを使えばいいじゃない

基本的な方針はVSCodeVimのキーバインドを変更し、`u`キーを押した際にVSCode本体のUndoが実行されるように設定することである。

```
"vim.normalModeKeyBindingsNonRecursive": [
        {
            "before" : ["u"],
            "commands" : ["undo"]
        },
        {
            "before" : ["<C-r>"],
            "commands" : ["redo"]
        },
    ],
```

この設定はこちらのコメントを参考にさせていただいた。参考にさせていただいたというか、丸パクリであるが。

<https://github.com/VSCodeVim/Vim/issues/3201#issuecomment-459515997>

ちなみに以前は[このIssueのコメント](https://github.com/VSCodeVim/Vim/issues/1490#issuecomment-352167221)にあるやり方でやっていたのだが、今回これを使ったら設定が正しく読み込まれずにVimプラグイン自体が動かなくなる羽目になってずいぶんハマってしまった。

## 設定ファイルに問題があることに気づくには

ちなみに私はVSCodeをクリーンインストールした後、設定ファイルを徐々に書き込みながら問題を絞り込んだ。単純に調べ方が分からなかったからだ。そしてこの問題を解決し終わってから、どうやったら設定ファイルにエラーがあることに気づけるかを知ったので、こちらも共有しておく。

VSCodeではDeveloper Toolsを開くことでデバッグ情報が確認できる。

- コマンドパレットを開いて`Toggle Developer Tools`を実行する
- メニューのHelp → Toggle Developer Toolsを選ぶ

まあElectron製のアプリケーションなのだから、この方法でデバッグ情報が確認できることにもっと早く気付けばよかった。(ずっとVSCodeのDebug Console見てた)

<https://github.com/VSCodeVim/Vim#debugging-remappings>