---
title: "Genymotionを導入してエミュレータの起動待ち時間を短縮する"
slug: 87
date: 2014-09-16
lastmod: 2014-09-20
tags: 
    - プラグイン
    - "Android Studio"
---

アプリ開発をしていてバカにならないのが、デバッグにかける時間です。頻繁にエミュレータを起動して動作確認を行うわけですが、デフォルトのエミュレータ（Android SDKのエミュレータ）はとにかく起動が遅いです。さらに動作ももっさりしていて、お世辞にも動作確認しやすいとはいえません。

そこで動作確認の時間をできるだけ短縮するためにも、Genymotionを導入しておくことをおすすめします。起動も早く動作もスムーズなので、デフォルトのエミュレータを使うのが馬鹿らしくなります。

私の環境で実際に両者を比較した動画を撮ってみました。

<iframe width="854" height="510" src="//www.youtube.com/embed/KEI7TPXVrfI" frameborder="0" allowfullscreen></iframe>


## Genymotionをインストールする


<a href="https://www.genymotion.com/">Genymotion</a>を利用するためには、ユーザー登録が必要になります。

また、エミュレータを動かすために別途<a href="https://www.virtualbox.org/">Virtual Box</a>が必要になります。


## 端末を登録する


Genymotionをインストールできたら、端末の登録を行いましょう。Genymotionは実在する端末のエミュレーションを行うものなので、よく使う端末をとりあえず登録しておけばいいと思います。

サポートするAndroidのバージョンに合わせて登録しておくといいでしょう。私はとりあえず、Android2.3の端末と、自分の持っているGaraxy S3を登録しています。

端末の追加はそんなに難しくありません。予め用意されている端末から、エミュレーターとして使いたいものを選択するだけです。

![Genymotionで端末の追加](6d472ec41f2d388d6d3cabb3d79ff338.jpg)

![Genymotion端末の選択](d641c3096b812d702aeec398f3bca22d.jpg)

![Genymotion端末の表示名を決める](694edb0798dc0be344b64e5a3f951dac.jpg)

![後はダウンロードを待つだけ](a1aa6cf59f36f8802c965f04b850ad8d.jpg)


## Android Studioでプラグインを導入する


Android StudioからGenymotionのエミュレータを起動するためにも、Genymotionのプラグインも一緒にいれましょう。別に入れなくても使用に問題はありませんが、入れておいたほうがエミュレータの起動が捗ります。

![GenymotionPluginからの端末起動](5400a415e9f2e65765ffebd9713db8cc.jpg)

こんな感じでAndroid Studioから起動しやすくなります。

インストールの仕方はAndroid Studioの`Preference > Plugins`からGenymotionを探してインストールするだけです。そうすることでAndroid Studioの右上にGenymotion用のアイコンが追加されます。

![Genymotion Pluginのインストール](e8da57855d868853e7c2d64a1bd5edd6.jpg)


## 万能ではないものの使わないのは損


Genymotionではデフォルトのエミュレータと比較して、画面サイズやAndroidのバージョン、SDカードの有無など細かなところまでカスタマイズすることができません。特にFreeライセンスでは利用できる機能に制限があるため、Android SDKのエミュレータを完全に置き換えるものではありません。

ですが基本的なデバッグ・動作確認にGenymotionを利用することで、アプリ開発における動作確認の時間を短縮することができると思います。基本的にはGenymotionを使うようにすれば、開発がだいぶ捗るのではないでしょうか？


  