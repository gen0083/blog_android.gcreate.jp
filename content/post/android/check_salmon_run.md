---
title: "サーモンランのスケジュール確認専用アプリを作った"
slug: "check_salmon_run"
date: 2019-01-07T17:54:00+09:00
tags:
    - マイアプリ
    - Firebase
---

ほぼサーモンラン専用となった私のSplatoon2のゲームライフを、より豊かにするために。サーモンランのスケジュールだけを確認できるシンプルなアプリを作成した。

<!--more-->

ちょっと前からSplatoon2を再開した。一度手放したのだけれど、今更ながらまた買ったわけである。

今も以前ももっぱらサーモンランで遊ぶだけ。へたくそ+ぼっちなもんで、レギュラーやガチマッチはほとんど遊んでいない。使いたいブキがあるのでランクを上げたいのだけど、そのランクが上がるまでが苦痛で続かないのだ。

それにしても、相変わらずスケジュール更新時に挟まれるハイカラニュースの存在が邪魔で仕方がない。なぜこれはスキップ可能になっていないのか。これのせいでSplatoon2を起動したままスリープしておくのが私のスタイル。他のソフトを遊ぶと必ずハイカラニュースを見なければならないので、できる限り終了したくない。

そんなハイカラニュースだが、できる限り出くわさないようにする方法がある。それはサーモンラン開催時間中にのみサーモンランを遊ぶというスタイルだ。サーモンラン閉鎖中はスイッチをスリープモードにしておくだけである。クマさん商会の中でスリープしておけば、基本的にはハイカラニュースの割り込みが発生しない(まあフェスの予告とかどうあがいても割り込まれることはあるのだけど)。

このことに気づいたため、できる限りサーモンラン開催中の期間のみアクセスするようにしたのだが、スケジュールを公式アプリで確認するのが非常に面倒である。サーモンランのスケジュールを見るのに3ステップ必要で、しかも各ステップ中での微妙な待ち時間があるのも悲しい。

そこでサクッとスケジュールだけ確認できるアプリを作った。<a href="https://play.google.com/store/apps/details?id=jp.gcreate.product.sachedule">https://play.google.com/store/apps/details?id=jp.gcreate.product.sachedule</a>

ほぼほぼ自分専用アプリである。

このアプリで私のサーモンランライフは快適になった。ハイカラニュースの割り込みでイライラしないという意味で。

## 技術的な話

技術的にはFirebase Functionsを使って非公式にSplatoon2のスケジュール情報を公開しているAPIに定期的にアクセスを行うような形をとっている。それぞれのアプリが個別にアクセスすると、さすがに先方に迷惑だろうと、アクセスするのはサーバ側だけに限定した。

無料プランでは、Firebase Functionsは外部へのアクセスができないため、一工夫している。自分のサーバからcronで定期的にプログラムを実行、Firebase FunctionsのAPIを叩いてスケジュール情報を更新している。

ついでに更新されたデータはFirebase Database(Realtime database)を利用してアプリに同期させている。そのためアプリ側では特に何もしてない。単にFirebase Realtime Databaseに接続しているだけという作りだ。見た目・中身ともにかなりシンプルなアプリである。

問題的には、非公式のAPIを使っているところなので、いつ更新が止まるかわからないというところが不安ではある。一応、最低限のアクセスで済むよう工夫はしたつもりであるが。後は仕様変更によってAPIが止まる可能性もありうるので、いつまで使えるかは不透明だ。

ただ個人的には、Firebaseの機能をまともに利用して公開したはじめてのアプリかもしれない。特にFuncitonsとの連携は面白かった。外部へのアクセスに制限がかかるが、工夫次第でいろんなことができそうである。