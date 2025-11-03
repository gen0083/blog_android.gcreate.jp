---
title: "Composeでborderの一部分を区切ったようなエフェクトをつける"
slug: "border_path_effect"
date: 2025-11-03T22:56:25+09:00
tags:
    - Compose
    - Kotlin
    - Android
---

ComposeでUIを実装するにあたり、borderを角丸の部分だけに描画するという要件が求められた。

<!--more-->

## drawBehindでpathEffectを使う

たとえばBoxにborderをつける場合、Modifierに`border`を指定すればborderをつけることができる。ただしこれでは単純なborderしか表現できない。

ところで点線で描画するといった手法であれば、PathEffectを使えば実現できる。これをうまく利用すれば角丸部分だけのborderが表現できそうだ。

```kotlin
    Box(
        modifier = modifier
            .size(50.dp)
            .background(color = Color.Red)
            .drawBehind {
                // floatで指定はpxの値なので、dp.toPx()でdpの値にして更にpxにする
                // cornerRadiusは x=8.dp, y=8.dpで指定するので、実際のコーナーの長さは直径は16*PI/4になる
                val cornerLength = (16 * PI / 4).dp.toPx()
                val effect = PathEffect.dashPathEffect(
                    floatArrayOf(
                        0.dp.toPx(),
                        34.dp.toPx(), // Boxのサイズが50で、角丸部分のyの高さが8*2なので、残りが直線部分
                        cornerLength,
                        34.dp.toPx(),
                        cornerLength,
                        34.dp.toPx(),
                        cornerLength,
                        34.dp.toPx(),
                        cornerLength,
                        0f,
                    ),
                )

                drawRoundRect(
                    cornerRadius = CornerRadius(8.dp.toPx(), 8.dp.toPx()),
                    color = Color.Black,
                    style = Stroke(
                        width = 1.dp.toPx(),
                        pathEffect = effect,
                    )
                )
            }
        ,
    )
```

`drawRoundRect`で描画する際に、はじめの位置は左下の直線部分からの指定になる。これが`drawRect`の場合は左上からの指定になる。ちょっとややこしい。

pathEffectで指定するFloatArrayは必ず2個1セットで指定する。奇数個だからといってエラーにはならないが、最後の指定が無視されてしまう。FloatArrayの指定は、描画する・しない（オンとオフ）の組になる。

phaseの指定もできる。phaseはFloatArrayの指定のどこから始めるかを指定する。

ここでは50.dpと固定のサイズでやったが、可変サイズにも対応可能である。

`drawBehind`のDrawScope内では、`this.size.width`や`this.size.height`で幅・高さを取得できる。これを使うことで可変サイズにも対応可能である。その際は単位に気をつけたい。
