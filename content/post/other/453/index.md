---
title: "flutterやるならぜひ登録しておきたいLive Template"
slug: 453
date: 2018-03-24
lastmod: 2018-03-24
tags:
    - flutter
    - "Android Studio"
---

Flutterを触り始めたのだが、とにかくWidgetのレイアウト変更がツライと感じていた。

AndroidでいうところのViewのレイアウトがコードでゴリゴリ書いていく感じになっているので、インデントが深くなってツライ。Widgetの考え方もAndroidのViewとはちょっと違う（レイアウトに関する設定はレイアウト情報を持つWidgetでくるむとか）

ゼロから作る分にはまだいいのだが、一度作ったレイアウトに対して、「このTextにmargin付け加えたい」となったときがツライ。シンプルなレイアウトならまだいいが、Widgetが何個も登場したり、何回層もネストされてたりすると正直触りたくない。

例えばこんな感じ。


```
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        title: new Text("FriendlyChat"),
      ),
      body: new Column(
        children: <Widget>[
          new Flexible(
              child: new ListView.builder(
                padding: const EdgeInsets.all(8.0),
                reverse: true,
                itemBuilder: (_, index) => _messages[index],
                itemCount: _messages.length,
              ),
          ),
          new Divider(height: 1.0,),
          new Container(
            decoration: new BoxDecoration(
              color: Theme.of(context).cardColor,
            ),
            child: new Text("hoge"),
          ),
        ],
      ),
    );
  }
```

これはまだかわいいものだが、それでもめんどうくさい。

そこでLive Templateを追加して、IntelliJのSurrond With機能を使って簡単にWidgetを囲えるようにしてみた。Flutterのチュートリアルを試したりするのに活躍するのでかなり捗ると思う。


## Live Templateを定義


Preference > Editor > Live Templateが定義場所。

定義する場所は別にどこでもいいのだろうけれど、Flutterに関することなのでFlutterのところに追加した。


```
new Column(
  children: <Widget>[
    $SELECTION$
  ]
),
```

Dartファイルに適用されるように指定して、Reformat according to styleにチェックも入れておく。

![Sample](sample.png)


```
new Container(
  child: $SELECTION$
),
```

childを1つしか取らないWidgetでラップする場合に使うやつもついでに追加。使っているのが`Column`と`Container`であることに特に意味はない。まあそこは必要に応じてクラス名を書き換えればいいだろうから気にしない。

Live Templateを定義したら、後は囲いたいWidgetを選択した状態で、Surround with機能を呼び出し（私の環境だとcmd+opt+t）、定義したLive Templateを適用すればよい。楽ちん。

![test movie](surround.gif)

Live Templateは初めて活用したので、もっとこうした方がいいよというのがあったら教えて欲しい。

追記:

記事を書き終わった後で、そもそも標準でWidgetをラップする機能が存在していることを知った。ラップしたいWidgetのクラス名にカーソルをあわせた状態で、Intention Actions（Macならopt+enterで出るやつ）を使うとWidgetを別のWidgetでラップすることができる。わざわざLive Templateを追加する必要はなかった・・・。


  