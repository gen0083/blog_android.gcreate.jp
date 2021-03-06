---
title: "AnimationDrawable 静止画を使ったアニメーション"
slug: 170
date: 2014-12-29
lastmod: 2014-12-29
tags:
    - Android
    - UI
---

静止画像（pngなどの画像リソース）を用意してパラパラ漫画の要領でアニメーションさせるには、AnimationDrawableクラスを利用します。

<a href="https://developer.android.com/reference/android/graphics/drawable/AnimationDrawable.html">Android APIs Reference &#8211; AnimationDrawable</a>

![AnimationDrawableのサンプル](24ee559b81887e42094def634c0c007e.gif)

文字が変わってるだけですが、3つの画像でアニメーションしてます。画像を準備するのが面倒くさかったので、文字だけの画像を使いました。


## アニメーションに使う静止画像


画像は解像度に合わせて`res/drawable/hdpi`などのディレクトリに用意します。

今回はanime_test1.png,anime_test2.png,anime_test3.pngの3つの画像ファイルを用意しました。画像と言いつつ数字の1,2,3が書かれているだけの画像です。

ちなみにファイル名として使えるのは小文字のアルファベット、数字、アンダースコア(_)とドット(.)のみです。それ以外の文字（大文字アルファベットなど）を使うと以下のようにコンパイルエラーとなります。

<blockquote>
  Invalid file name: must contain only lowercase letters and digits ([a-z0-9_.])
</blockquote>

## アニメーション設定のXMLファイル


どの画像を何秒間表示させるのかという設定をXMLファイルに記述します。今回は`res/drawable/test_animation.xml`というファイル名にしました。


```
<?xml version="1.0" encoding="utf-8"?>
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="false">
    <item android:drawable="@drawable/anime_test1"
          android:duration="500"/>
    <item android:drawable="@drawable/anime_test2"
          android:duration="500"/>
    <item android:drawable="@drawable/anime_test3"
          android:duration="500"/>
</animation-list>
```

`android:oneshot=true`で、アニメーションを1回のみ再生する設定になります（最後の画像でアニメーションが止まる）。falseだとループ再生されます。


## アニメーションを再生する


test_animationは何もしなければ単なる静止画と同じで、Drawableとして扱うことができます。ImageViewのsrc属性に設定したり、TextViewのbackground属性に設定したりすることができます。

今回はImageButtonに上記で作成したdrawableを設定してやり、ボタンを押したらアニメーションが再生されるようにしてみます。

activity_main.xml


```
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
                xmlns:tools="http://schemas.android.com/tools"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                tools:context=".MainActivity">

    <ImageButton
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/image_button"
        android:src="@drawable/test_animation"
        />

</RelativeLayout>
```

APIリファレンスでは`android:background`属性に設定していますが、これは`android:src`属性に設定しても動きました。src属性にAnimationDrawableを設定した場合、`getBackground()`ではなく`getDrawable()`でAnimationDrawableを取得します。

MainActivity.java（onCreateを抜粋）


```
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageButton imageButton = (ImageButton) findViewById(R.id.image_button);
        final AnimationDrawable animationDrawable = (AnimationDrawable) imageButton.getDrawable();

        imageButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                animationDrawable.start();
            }
        });
    }
```

AnimationDrawableを取得して、start()メソッドを呼び出せばアニメーションさせることができます。

ただしできるのは再生するか停止するかくらいで、逆再生したりはできないみたいです。


  