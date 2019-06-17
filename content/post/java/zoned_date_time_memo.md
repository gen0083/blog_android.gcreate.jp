---
title: "ZonedDateTime覚書"
slug: "zoned_date_time_memo"
date: 2019-06-17T17:37:16+09:00
tags:
    - Java
    - ZonedDateTime
---

私はアプリ内で時刻を取り扱う際には、基本的にZonedDateTimeを使うようにしている。しているのだが、基本のセットアップをした後はあまり複雑なことをしない。そのため別プロジェクトで新たにセットアップをする際、いつも「あれ、どうやるんだっけ」となってしまう。

一応個人的メモは持っているものの非効率なので、よく使う設定を覚書としてメモしておこうと思う。ちなみにAndroidで使う場合の話をメインにするが、JavaでZonedDateTimeを扱うときと基本は同じだと思う。

正直なところ理解があやふやな部分もあるので、間違いがあったら指摘してほしい。

<!--more-->

## セットアップ

まずはセットアップ。AndroidでZonedDateTimeを使おうと思ったら、[ThreeTenABP](https://github.com/JakeWharton/ThreeTenABP)を使うことになるだろう。

build.gradleに依存を追加して・・・というあたりは割愛する。

ちなみにカスタムApplicationクラスにおいて`AndroitThreeTen.init(this)`で初期化するのをよく忘れる。Zone DBが初期化されていないというエラーとともにアプリがクラッシュするので気をつけよう[^1]。

## ユニットテストをする際には本家を使う

Robolectricを使ったユニットテストをするのであればたぶん問題ない話かもしれないが、JVMのユニットテストでZonedDateTimeを使ってテストを書く場合には一工夫が必要である。

ThreeTenABPは、TimezoneのDBをApplicationクラスで初期化してはじめて使えるようになる。ということは、Applicationクラスを経由しないユニットテストではTimezoneのDBが存在しないことになってしまう。

回避策はテストの際は[threetenbp](https://github.com/ThreeTen/threetenbp)を使うというだけだ。`testImplementation "org.threeten:threetenbp:1.3.1"`(バージョンは適宜調整されたし)と、テストでは本家の依存を追加することで回避できる。

まあ[このissue](https://github.com/JakeWharton/ThreeTenABP/issues/14)を見て私はそうしているというだけである。

## データベースへの保存

ZonedDateTimeをアプリケーション内で扱うとして、DBにはそのままでは保存できない。何らかの形で変換が必要だ。

変換先をどうするかは人それぞれだろうが、私は`Long`を選ぶことが多い。で、困ったことにこの`Long`への変換・復元操作が一筋縄ではいかないので毎回困るのである。(忘れているという意味で)

まず大前提として、アプリケーション内で扱う時刻はすべてUTCに変換して扱う。Longへ変換は、つまるところepochSecondへの変換なのだが、ここではTimezone情報が抜け落ちる。だからLongへ変換する際には必ずタイムゾーンをUTCに変換してから処理を行う。

私は毎回こんな感じで拡張関数として定義しておく。

```kotlin
fun ZonedDateTime.toUtcLongMillis(): Long {
    val utcZDT = this.withZoneSameInstant(ZoneOffset.UTC)
        .truncatedTo(ChronoUnit.MILLIS)
    return utcZDT.toInstant().toEpochMilli()
}

fun Long.toZonedDateTimeUtc(): ZonedDateTime {
    val instant = Instant.ofEpochMilli(this)
    return ZonedDateTime.ofInstant(instant, ZoneOffset.UTC)
}
```

注意することというか、補足することは次のようなこと。

- `withZoneSameInstant(ZoneOffset.UTC)`でUTCでの時刻に変換する
- `truncatedTo()`でナノ秒以下を切り捨てているのは別にいらないかも[^2]
- 一度`Instant`に変換してから`toEpochMilli()`でミリ秒(Long)に変換する
- 復元する際は`ofEpochMilli`でLongからInstantに変換した後、そのInstantからZonedDateTimeを復元する

## Instantとはなにか

Instantは私の理解では、刻々と変化する時間のとある一時点を示す情報だ。しかしその「とある一時点」は、具体的に何年何月何日の何時何分何秒なのかは不明である。その情報はタイムゾーンが指定されることではじめて分かるからだ。

時間には時差があるので、時差の情報はタイムゾーンが指定されなければ分からない。時差が分からなければ、「とある一時点」だけ伝えられても、時差次第でどうとでも変化してしまうからだ。同じInstantでもUTCでは2019年6月17日の9時8分5秒であり、日本(JST)では2019年6月17日の18時8分5秒だからだ。

そのためZonedDateTimeは時間の一時点を表すInstantと、タイムゾーンに関する情報の2つを持つようになっている。

そもそも時間の概念がややこしい。ZonedDateTimeを扱うようになってから余計にそう思うようになった。


[^1]: 気をつけようといっている本人は、ThreeTenAbpを新規でセットアップする際はほぼ毎回やらかしている。
[^2]: どうせ`toEpochMilli`で切り捨てられるため
[^3]: `ofEpochMilli()`でInstantを作るなら`toEpochMillis()`みたいなのがあってしかるべきでは？