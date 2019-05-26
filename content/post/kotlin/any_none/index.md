---
title: "リスト内に一定の条件に属する要素が存在するか否かを調べる"
slug: "any_none"
date: 2019-05-26T11:25:12+09:00
tags:
    - Kotlin
---

例えばIntの配列の中に特定の条件を満たす要素が存在しているかどうかを調べたいとする。
今回はそんなときに使える標準関数を紹介する。

<!--more-->

## いままでどうやっていたか

<iframe src="https://pl.kotl.in/3QJT8ccbY?theme=darcula"></iframe>

私は`filter`関数の存在をしっていたので、これで条件に合致するものが存在するかをしらべ、filterの結果が空なら条件に合致するものがないと判断していた。

まあこんな書き方をすると、最近のKotlinは賢いので「それ、こう書けますよ」と教えてくれるのがすごい。

## any / none

何らかの判定式を用いて、リスト内の要素に条件に合致するものが存在するかどうかを調べる場合、`any`や`none`関数が利用できる。

`any`は判定式に合致する要素が1つでも存在すれば`true`を返す。
<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/any.html>

`none`はその反対で、判定式に合致するものが存在しない場合に`true`を返す。
<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/none.html>

<iframe src="https://pl.kotl.in/C8vUviYmz?theme=darcula"></iframe>

配列やListなどの要素に対して、特定の条件式を用いて判定を行う際に便利な関数である。