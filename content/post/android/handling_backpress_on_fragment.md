---
title: "Fragmentでバックキーのハンドリングを行う"
slug: "droidkaigi2020_1_handling_backpress_on_fragment"
date: 2020-01-17T21:35:25+09:00
tags:
    - Android
    - Kotlin
    - Fragment
---

久しぶりのAndroid開発である。Droidkaigiのアプリが公開されたので今年もコントリビュートしようと挑戦した。今回はFragmentでバックキーのハンドリングを行うことに挑戦した。

<!--more-->

## 問題点

今回取り組んだissueはこれ。

https://github.com/DroidKaigi/conference-app-2020/issues/126

Droidkaigiのアプリではバックドロップで表示するセッションのフィルタリングをするようになっている。このバックドロップが表示されている状態（以降Filterが表示されてる状態と呼称する）において、バックボタンを押したらセッションが表示されるようにしてみてはという内容である。

Material Design的にどうするべきかは知らない。しかし私もバックボタンでセッション一覧を再表示するほうが自然なように思う。

## onBackPressedDispatcher

解決策は単純で、バックキーを押したときの処理を上書きしてやればよい。

しかし件の画面はFragmentである。`onBackButtonPressed()`があるのはActivityなので、Fragmentでバックキーの挙動を上書きするには、これまではinterfaceを噛ませてイベントを伝播させるしかなかった。

しかし今ではFragmentからでもハンドリングできるようになったようだ。[公式ドキュメント](https://developer.android.com/guide/navigation/navigation-custom-back)にもあった。

```
requireActivity().onBackPressedDispatcher.addCallback(this) {
    // Handle the back button event
}
```

なるほど、このような便利なものができたのかと早速使ってみた。しかし意外とこれが曲者だった。

## onBackButtonPressedとは違う

Activityでよくやる`onBackButtonPressed()`と同じような感覚で使おうとすると、ちょっと挙動が違うのでハマることになる。どうも考え方が根本的に違うようで、こちらは本当に必要なときにだけ有効にする、という感じで扱うもののようだ。

というのもこのcallbackが有効である限り、バックボタンの処理はFragmentで設定したcallbackが奪ったままになる。Activityの`onBackButtonPressed()`におけるsuperを呼び出す処理に該当するものが見当たらない。

[ソースコードを見てみると](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-master-dev:activity/activity/src/main/java/androidx/activity/OnBackPressedDispatcher.java;l=192)、コールバックが有効なものがある場合、その処理を呼び出してバックボタンが押された処理は終了される。

Activityでやるようにデフォルトの挙動を呼び出すことができない。登録されたままにしてると、それが全部イベントを奪うのでホーム画面に戻れない。UIの状態によってバックボタンの挙動を変えたい場合、状態によってcallbackの有効・無効を切り替えなくてはならない。

[こちらの記事](https://qiita.com/SorrowBlue/items/9723120a7020bdd49b7c)にあるように、コールバック内で`isEnabled`を変更するという手も利用してみたが、状態によって切り替えたい場合コールバック内の切り替えだけではうまくいかなかった。

私の実装の仕方が悪かったのかも知れないが、コールバック内でBottomSheetBehaviorの状態をチェックして`isEnabled`を切り替えると、バックボタンを余計に押さなくてはならなかった。振り返ってみれば、たぶん実装の仕方が悪かったのだと思う。どちらにせよその方法では、Pagerで複数のFragmentを使っていると、うまく処理できなかったように思う。

`onBackPressedDispatcher.addCallback()`で登録したコールバックは、FragmentがDESTROYされると自動的に削除される。ついでにFragmentがSTARTしてる、もしくはRESUMEしてるときのみ処理を行うといったことをしてくれてれば楽だったのにと思った。

しかしないものはしょうがないので、`onPause`に入ったらコールバックを無効にし、`onResume`でフィルタが表示された状態ならコールバックを有効にするようにした。

処理自体は大したことをしていないにも関わらず、意外とハマってしまった。Androidアプリ開発が半年以上振りくらいになるので、ブランクがあった分の洗礼を受けた気分である。