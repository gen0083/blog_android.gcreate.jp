---
title: "VSCodeVimのundo設定"
slug: "vim_undo_old"
date: 2018-06-16T20:58:00+09:00
tags:
    - VSCode
    - 設定
---

Visual Studio Code＋Vimプラグインを使っていて、undoを使った際に想定より大きくundoされてしまって使いづらい。

Vimプラグインにおける<code>u</code>と<code>Ctrl+r</code>によるundo/redoを、Visual Studio Codeのundo/redoにマッピングすることで対策できる。

<a href="https://github.com/VSCodeVim/Vim/issues/1490#issuecomment-352167221">https://github.com/VSCodeVim/Vim/issues/1490#issuecomment-352167221</a>

User Settingsで"vim.otherModesKeyBindingsNonRecursive"を追加して、上記コメントにある設定を加えれば解決する。