---
title: "デザインを考える"
slug: 72
date: 2014-09-13
lastmod: 2014-09-18
tags: 
    - UI/UX
    - マイアプリ
---


## ださいデザインからの脱却


1分間タイマーは、最初のバージョンでは文字とボタンだけが表示されている、非常にダサいアプリでした。それに比べると現在の見た目はだいぶましになったように思います。あくまで最初の頃よりはましになったなというだけで、カッコイイ見た目にするにはどうすればいいのかよく分かりません。

ただ、見た目をかっこ良くするという観点からのアプローチは難しくとも、使いやすくするという観点からのアプローチであれば、少し突破口が見えるような気がします。私がSmashing Android UI レスポンシブUIとデザインパターンという本を読んで、1分間タイマーに加えた変更を例にしてみましょう。

<div data-role="amazonjs" data-asin="4844334514" data-locale="JP" data-tmpl="" data-img-size="" class="asin_4844334514_JP_ amazonjs_item"><div class="amazonjs_indicator"><span class="amazonjs_indicator_img"></span><a class="amazonjs_indicator_title" href="#">Smashing Android UI レスポンシブUIとデザインパターン</a><span class="amazonjs_indicator_footer"></span></div></div>

## 開始ボタンを押しやすくする


<em>1分間タイマーを自分で使っていてとても不便だったのが、タイマーの開始ボタンが押しづらいことでした</em>。

1分間タイマーの当初のバージョンでは、デフォルトのButtonを開始ボタンとして利用していました。私はタイマーを開始させたらすぐに紙に向かって文字を書き出していきたいため、アプリの開始ボタンは横目で見ながら押すような感じで使っていました。しかし以前のバージョンの四角い小さなボタンでは、<em>開始させたつもりが押せていないということがよくあってテンポが悪かった</em>のです。

ボタンを大きくすれば使い勝手はかなり向上します。

![新旧1分間タイマーの変化](sinkyu-1timer.jpg)


## 残り時間の表示方法


ボタンの巨大化にともなって、残り秒数の表現方法も変えることにしました。開始ボタンを円形にしたので、その周りにバーのような感じで残り秒数が分かればスマートかなと考えました。

以前は単に文字で残り秒数を表示していました。しかし自分で使っていて、あと何秒残っているかを文字で読み取ることはいままで一度もありませんでした。そもそも音声による通知もあるので、残り秒数を文字で把握する必要性はありません。

円形のバーであれば視覚的に横目であとどれくらい残っているかが分かるので、文字で表示されるよりもマシだと思います。

ただ、このバーの動きがカクカクしているのが残念なところです。スムーズに動くように見せることができれば、見た目もよくなるのですが、実装方法が分かりませんでした。いずれやり方を調べて実装できたらいいなぁと思っています。


## アプリ終了時の確認ダイアログをなくした


<em>以前のバージョンでは、バックボタンを押した時に「終了しますか？」という確認ダイアログを表示していました</em>。この終了するかどうか確認をとるアプリは、世の中にまだまだ多く存在しています。

みなさんは、アプリを使っていて終了時に確認ダイアログが出ることについてどう考えていますか？

「そんな確認はいらないんでさっさと終了しろよ」派でしょうか、「わざわざ確認してくれて親切やね、ありがとう」派でしょうか。

Smashing Android UI レスポンシブUIとデザインパターンでは、この終了時に確認ダイアログを出すのは、多くの場合開発者の都合によってつけられているものであると断じていました。


### 確認ダイアログは悪である


終了時に限らず、何らかの操作を行う際に確認ダイアログを表示するのは、<strong>取り返しの付かないことを実行する場合にユーザーに責任を転嫁させるため、開発者の都合で使われている悪しきものだ</strong>とバッサリでした。

確認ダイアログを出したところでユーザーがちゃんと確認するかどうかは分かりません。操作ミスを恐れて確認ダイアログを表示させるという考え方もあるかもしれませんが、そのダイアログのボタンを操作ミスしないとは言い切れないはずです。

そこで確認ダイアログを使うくらいなら、<em>操作を実行した後にそれを取り消すための手段をユーザーに提供することこそが、真のユーザーフレンドリーである</em>とこの本には書いてありました。ごもっともだと思いました。

終了時の確認で言えば、一度終了してしまうと起動するのに膨大な時間がかかってしまうため、操作ミスによる終了を防止する意味で出すというのはありかもしれません。起動するのに1分かかるゲームアプリで、やっと起動したと思った時に手が滑ってバックボタンを押してしまった。そういう場合であれば、確認ダイアログを表示する方が親切かもしれません。

ですが、その確認ダイアログは必要なのかと自問することが大切です。終了前の操作状態を復元することで対処できないか、いつ終了されてもデータが保存されるように作ればすむ話ではないか。そう考えることで使い勝手が向上していくのです。


## アプリのデザインは難しい


デザインといえば見た目の話だけだと思っていましたが、使い勝手に関わるすべてのものがデザインです。アプリの開発と一口に言っても、プログラムのことだけではなく、使い勝手のことについても考えなければなりません。実際にやってみると奥が深いなぁとつくづく思います。

今まで「デザイン」というと見た目をカッコよくすることだと思っていましたが、考えることはそれだけではないのだということが分かりました。<em>見た目をカッコよくするのは難しくても、使いやすくすることであれば考えれば何とかなりそうです</em>。

そんな見た目がおしゃれなデザインの話より、使い勝手を重視したデザインの話がいっぱいなSmashing Android UI レスポンシブUIとデザインパターン。読んでいるといろんな発見があると思います。

<div data-role="amazonjs" data-asin="4844334514" data-locale="JP" data-tmpl="" data-img-size="" class="asin_4844334514_JP_ amazonjs_item"><div class="amazonjs_indicator"><span class="amazonjs_indicator_img"></span><a class="amazonjs_indicator_title" href="#">Smashing Android UI レスポンシブUIとデザインパターン</a><span class="amazonjs_indicator_footer"></span></div></div>

  