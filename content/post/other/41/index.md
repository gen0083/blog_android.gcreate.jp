---
title: "Android Studioの便利なところ〜Gradleが便利〜"
slug: 41
date: 2014-09-05
lastmod: 2014-09-18
tags:
    - Gradle
    - "Android Studio"
---

Android Studioは、Gradleが便利だとよく言われています。

私がAndroid Studioを使い始めた頃は「Gradle便利っていうけど、どう便利なんだろう」とさっぱり分かりませんでした。むしろGradleが何をやっているか、何者なのかさっぱり分からず、逆によく分からない存在でした。（でしたというか、現在進行形でよく分かっていませんが・・・）

実際にGradleが便利というのが実感できたのは、外部ライブラリを簡単に取り込めることが分かってからです。


## 外部ライブラリの取り込み


Androidではアプリ開発に便利なライブラリが多数公開されています。

自分で1から作るより、すでにある便利なライブラリのお世話になった方が、アプリ開発スピードも早くなりますしクオリティも高くなります。

Android Studioではそういったライブラリを、build.gradleに1行記述するという簡単な方法で自分のプロジェクトに取り込むことができます。

デフォルトではbuild.gradleは2つあるのですが、いじるのはプロジェクト直下にあるものではなく、appディレクトリにあるbuild.gradleです。

![いじるbuild.gradle](7af2b259ceaaa2c853d831a993b66bca.jpg)

例えばcroutonというToastをカスタマイズして使える便利ライブラリを取り込む場合は、app/build.gradleのdependanciesに`compile 'de.keyboardsurfer.android.widget:crouton:1.8.4'`と記述をするだけで取り込めます。

`app/build.gradle`


```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    compile 'com.android.support:appcompat-v7:19.+'
    compile 'de.keyboardsurfer.android.widget:crouton:1.8.4'
}
```

Sync Project with Gradle Filesを実行すると、External Librariesに目的のライブラリが取り込まれます。

![External Libraries](External-Libraries.jpg)

あらゆるライブラリがこの方法で使えるとは限りませんが、非常に便利です。

アプリ開発の始めの頃は外部ライブラリを利用するなんて発想がなかったものですから、Gradleが便利だぞと言われてもなんのこっちゃとさっぱり理解できませんでした。しかし、実際にこうやってライブラリが簡単に取り込めるのを確認すると、「なるほど、こりゃ便利だわ」とAndroid Studioを使うのが楽しくなってきました。


  