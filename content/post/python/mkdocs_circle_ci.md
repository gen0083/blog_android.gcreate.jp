---
title: "mkdocs+CircleCIでmarkdownで書いた文書を自分のサーバにデプロイ"
slug: "mkdocs_circle_ci"
date: 2018-05-24T12:40:00+09:00
tags:
    - Python
    - MKDocs
---

Google Playで公開しているアプリのプライバシーポリシーの管理をもうちょっとらくできないかなと思って作業を始めた。

<!--more-->

<ul>
 	<li><a href="http://www.mkdocs.org/">MkDocs</a>を使う</li>
 	<li>リモートリポジトリとしてBitBucketを使う</li>
 	<li>CircleCIでビルド</li>
 	<li>自分のサーバにデプロイ</li>
</ul>

という環境を構築した。

MkDocsは特にこだわりがあったわけではないが、まあプライバシーポリシーをmarkdownで書けてHTMLで公開できれば何でも良かった。

軽く触ったところ <a href="https://squidfunk.github.io/mkdocs-material/">マテリアルデザインなテーマ</a>を簡単に組み込めるのがよい。デザインに脳みそを割かなくていいのは楽だ。

苦労したのはCircleCIの設定だ。

ローカルでは<code>mkdocs serve</code>でレンダリングの確認だけして（おそらく最終的にはそれすらしなくなるだろうけれど）、リモートリポジトリにpush、CircleCIで<code>mkdocs build</code>して、最後にビルドされたHTMLをscpを使って自分のサーバにアップロードするという方針。

私のサーバはユーザ名＋パスワードによる認証は許可していないので、公開鍵認証を使うのだが、この設定がうまくいかなくて困った。

そもそもscpで転送するのに使う鍵のファイルを指定するのにハマった。

<a href="https://circleci.com/docs/2.0/configuration-reference/#add_ssh_keys">add_ssh_keys</a>でCircle CIに登録したSSH認証鍵のフィンガープリントを追加してやる必要があった。これをしないと、deploy用のスクリプトから認証に使う鍵が参照できない。

そこをクリアしたら今度は別の問題でハマる。

Circle CIからscpで自分のサーバに接続する際に、<code>Are you sure you want to continue connecting (yes/no)?</code>で止まってしまうのである。known_hostsにないからというのは分かるが、どうやってそれを登録するのかというのがわからなかった。
なんとも頭のわるいやり方ではあるが、以下の方法で乗り越えた。

<ol>
 	<li><a href="https://circleci.com/docs/2.0/ssh-access-jobs/">ssh経由のデバッグ</a>を利用してCircle CIにログイン</li>
 	<li>sshコマンドを使って手動でログインを行いknown_hostsに登録</li>
 	<li>登録される文字列をCircle CIの環境変数に保存</li>
 	<li>該当文字列をknown_hostsに追記するスクリプトをscpコマンド実行前に追加</li>
</ol>

何かもっとちゃんとしたやり方があるような気がするのだが、私の英語力では解決策を見つけることができなかった。まあデプロイは無事にできるようになったので、文書の中身を練るとしよう。