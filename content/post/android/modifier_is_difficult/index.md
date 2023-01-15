---
title: "Modifierの適用順序、難しすぎん？"
slug: "modifier_is_difficult"
date: 2023-01-15T17:04:13+09:00
tags:
    - Kotlin
    - Android
    - Jetpack Compose
---

最近になってようやくJetpack Composeを触り始めた。

はじめはとっつきにくいなあ、レイアウトはXMLでいいじゃんとか思っていたのだが、慣れてしまえば不思議なものである。レイアウト見るためにいちいちXMLファイル見に行くほうが面倒くさいじゃんと今では感じるようになった。

しかしJetpack Composeでもよくわからないことがある。それがModifierである。

<!--more-->

## Modifier難しすぎる問題

Modifierが難しい。未だに慣れないものの1つが`Modifier.align()`である。実はあるScope内での拡張関数として定義されているようで、それで`Row`では使えるけど`Column`では使えないとかが起こるらしい。というのは分かったが、相変わらず混乱することに変わりはない。

今回の本題はModifierは適用順で効果が変わること、である。

例えばこのようなレイアウトを組みたいとする。角丸のコンポーネントを並べる感じにしたい。

![角丸白背景のコンテンツが並ぶ画像](layout_sample.png)

だが上2つはシャドウが効いていなくて、下2つはシャドウが効いている。効いていないコードはこうである。

```
    Column(
        modifier = Modifier
            .clip(RoundedCornerShape(8.dp))
            .shadow(4.dp)
            .background(Color.White)
            .padding(8.dp),
    ) { ...
```

クリップしてからシャドウつけるとうまく動かない。clipとshadowを入れ替えると　ちゃんと描画されるようになる。

https://github.com/gen0083/ComposeSample/blob/main/app/src/main/java/jp/gcreate/sample/composesample/ui/column/NormalColumnLayout.kt

Modifierでチェインしてカスタマイズするよりも、Surfaceで描画したほうが楽な気がしている。

そもそも外部から受け取ったModifierを上書きして使っているのよくないらしい。

何となく雰囲気でModifierを設定しているが、思ったとおりに行かなかったりすることもあって大変だ。

そもそもこういうレイアウトを組もうと思ったら`Surface`を使ったほうがいいのだろうか。パフォーマンスにも影響してきたりすると大変である。

本当はもっと深堀りして調べたかったのだけれど、時間が色々と足りないのである。適用の順番でShadowが出たり出なかったりがあるので、気をつけたいというのが今回の気づき。