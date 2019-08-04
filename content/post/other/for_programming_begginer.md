---
title: "プログラミング初学者のよく陥りがちなパターンについて"
slug: "for_programming_begginer"
date: 2019-08-03T14:47:21+09:00
tags:
    - プログラミング
    - 学習
    - ポエム
---

プログラミングを学習している人をサポートしたりしてるんだが、そのときに思うことがある。今回はその1つである、どこぞのブログを参考にしてやりましたパターンについて語ろうと思う。

<!--more-->

## HowTo的なブログを参考にすることの是非について

私は是である。なぜなら私も利用するので。ただ、それはある程度プログラミングがわかっているからできることであることは覚えておいて欲しい。

「ふーん、そういう感じならここは参考になりそう」みたいに、参考にすべきところを把握して、書いてあることを鵜呑みにしたりはしない。自分がやってるプロジェクトに合わせて、変更すべきところがどこかもだいたい当たりがつけれる。だからありがたく利用できるところを利用させていただくのである。

しかしこれが初学者だと話は変わる。初学者は書いてあるとおりにしかできない[^1]ので、それでうまくいっているうちはいいが、どこかで躓くとどこをどう直していいかわからなくなる。さらにググって自分でなんとかしようとして、魔改造が起こる。こうなると、それを解決する側も紐解くのが大変である。

もっとも私の場合、初学者よりましな自称プログラマー程度のレベルなので、エキスパートはもっとさらっと答えられるのだろうなぁなんて考えてしまう。特に問題の原因がどこにあるかをしっかりと把握せずに、気になったところをいじってしまうので、余計に時間がかかる。

エキスパートであればどこが問題で、どこが原因かすぐに把握し、さっと回答してしまえるのだろう。ただ、初学者の対応はすごいエネルギーを使うので[^2]、質問サイトとかで回答を続けている人には頭が下がる思いである。

しかしプログラミングに挑戦する人に手を差し伸べるのは、自分の勉強になるこにもなるし、何より仲間が増えるのは嬉しいことだ。だからこそできるんだろうなと思う。

## どうしたらよいか

HowTo的なブログを利用して学習をすすめることについて異議はない。が、やはりあわせて公式ドキュメントに当たるべきである。英語だからと毛嫌いする気持ちも理解できなくはないが、それでも読まないというのであればあなたはプログラマには向かないのではないだろうか。

英語が話せるようになれとは言っていない。ただ、英語を毛嫌いするなとただそれだけだ。読めるようになれとも言わない[^3]、ただ読む努力をしようよという話である。そもそもプログラムの公式ドキュメントは英語の中でも読みやすい部類のはずなのだ。コードが書いてあるからなんとなく雰囲気がわかるから。

それに公式ドキュメントにはQuick Startといった情報もあるし、HowTo的なブログでサラッと書かれていた重要な要素・オプション設定についての説明が書かれているのである[^4]。

## 小さくすすめる

初学者がやりがちなのが、いきなり自分の作りたいものを作り始めるパターン。これに関する是非は難しい。自分の作りたいものを作るのが一番モチベーションにいいのは間違いない。ただ、いきなり複雑な問題に立ち向かおうとするとわけがわからなくなるのも事実。

少なくとも私は、自分の作りたいものを作っていくにしても、はじめて扱う要素についてはそれ専用のプロジェクトを用意して使い方などを学ぶほうがいいと思っている。

Androidでいえば、RecyclerViewでリスト表示が必要なことがわかったときに、いきなりRecyclerViewを自分のプロジェクトに組み込むのではなく、RecyclerViewの使い方を学ぶための別プロジェクトを作れという話だ。

この手の問題は、issue報告する際に問題が発生する最小構成のプロジェクトを用意することが推奨されるところに近いものがあるだろう。

まずはシンプルな形で使い方を学び、そこから自分のプロジェクトに組み込んでいけばいい。そうすることで、シンプルなやつではうまくいったのに、自分のプロジェクトではうまくいかない状況に遭遇したとき、どこに問題があるか切り分けしやすくなる。

## プログラムの学習とは

以前書いたが、プログラミングは自分の解決したい問題を、コンピュータが解決できる形に変換する作業だというようなことを書いたと思う。

ここでコンピュータが解決できる形に変換するためには、コンピュータができることを知らなければならない。どう書いたらどう動くかを知る必要がある。

言い換えればプログラミング言語の学習では、その言語でどういったことができるのかを学んでいくことが大事であるということだ。プログラムでできることがわかってきて、はじめてでは自分の解決したい問題を、コンピュータに解決させるにはこうしようという思考ができるようになるのだ。

初学者の人は、そのプログラミングでできることを学ぶ、引き出しを増やすという作業を怠りがちなのではないかと私などは感じてしまう。Hello Worldとかめんどうくさいと思うだろう。ちなみに私も面倒くさいと思う。でも、あれはあれでやっぱり大事なのだ。そのプログラミング言語でできることを学ぶ第一歩として、どうやれば動くのかを知るためのものなのだから。

プログラミングは地味でわからんというのであれば、たぶんやっぱりあなたはプログラマには向かないと思う。少なくともコピペプログラマ止まりになってしまうのではないだろうか。

プログラミングは地味な作業だ。地道にできることを学び、引き出しを増やしていき、それを積み上げて自分の作りたいものを作り上げる。ピラミッドを組み上げる作業のようなものだ。ショートカットするのもいい。ただ、その建築物の屋台骨はぐらついている。

## 結局何が言いたいか

- 公式ドキュメント見よう
- 小さくやってみよう

以上2つである。

ただ間違えてほしくないのだが、自分のやりたいことや作品が決まっているのであれば、それを完成させるために邁進すればよいのだ。そこは間違えないで欲しい。別に遠回りして、地味なところを全部やってからやれと言っているのではない。

ただその進み方は、複雑な問題をより複雑にしやすいことは頭の隅に置いておいてほしい。わけがわからんなと思ったら、一度立ち戻って、スモールスタートしてみてはいかがだろうか。

こうやればこうなるはずだと考えるのは危険である。だいたいこの考えによって私はかなりの時間を浪費している。そんなときは原点に返って公式ドキュメントを読むと解決したりするのだ。そこを怠るからムダにハマるのだ。

後はエラーメッセージをちゃんと読もうとかもあるけど、話が長くなるので今回はここまで。

[^1]: たまに書いてあるとおりにすらしない人もいるが
[^2]: 質問のお約束が守られていない、情報が足りない、質問の意図が我々では理解できないなど。
[^3]: そもそも私も読めるとは言えない。雰囲気でやっているだけである。
[^4]: そもそもドキュメントにすら書いてないこともある。そういうのはどうするかいうと、ソースコードを見るのである。