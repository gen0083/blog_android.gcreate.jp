---
title: "Android StudioでQuick Documentationを活用する"
slug: 259
date: 2015-04-28
lastmod: 2015-04-28
tags:
    - "Android Studio"
    - ショートカット
---

Android Studioでコーディングしていて、「このメソッドどういう処理するんだっけ？」と思った時に便利なQUICK DOCUMENTATIONがあります。

F1押すと出てきますが、標準だとFloating Modeで表示されて邪魔です（設定によって違うかもしれませんけど）。

![Floatingモードで表示されて邪魔](c91be55cdf2a12d2d23a0f17ad06367c.jpg)

これは右上の歯車マークをクリックして、Floating Modeを押して解除してやれば他の枠に収まってくれます。

![Floating Modeを解除](9ad880f1afc2b3108a7619f837384957.jpg)

私の場合毎回右側にDocumentationが収まるのですが、右側は個人的に見づらい。このDocumentationはドラッグすることで表示位置を移動することができます。

個人的には右下に置いておくのが好みです。

![表示位置は調整可能](0b0038a904d5e052d27fd081c87fa7fc.jpg)

こうすることでQuick Documentation機能がぐっと使いやすくなります。

これでめでたしめでたしなんですが、このままではDocumentationの表示位置は現在開いているプロジェクト固有の設定にしかなりません。

つまり、別のプロジェクトを作成してQuick Documentationを利用した時に、再びFloating Modeで開かれてしまいます。プロジェクトごとに毎回この設定をするのは面倒なので、これを標準のレイアウトとして設定してしまいましょう。

方法はAndroid StudioのWindowメニュー→Store Current Layout as Defaultを選べばOKです。

![標準のレイアウト設定にしてしまう](e80a88cc1a14dd5dfd7b355871ea8c94.jpg)

これで毎回設定せずともすみます。


  