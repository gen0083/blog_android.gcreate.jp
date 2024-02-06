---
title: "Droidkaigiのリポジトリを参考に自分でGradle Pluginを作成してみる"
slug: "gradle_share_my_plugin"
date: 2024-02-05T19:02:28+09:00
tags:
    - "Android Studio"
    - Kotlin
    - Gradle
---

Droidkaigiのリポジトリのように、マルチプロジェクトで設定ファイルを共有する仕組みを知りたいと思って幾星霜。

今まで重い腰が上がらなかったのだが、Wear OSのプロジェクトが設定をベタ書きにしており非常につらい思いをしていたので、必要に迫られてやることにした。誰かの参考になれば幸いである。

<!--more-->

## 用途

Droidkaigiのリポジトリを参考にGradle Pluginを書いている。1度書いてしまえば使い回せるし、非常に便利だ。特にマルチプロジェクト構成だとその恩恵は大きい。

例えばWear OSのプロジェクトであれば、WearとMobileとモジュールが別れてしまう。両者で共有モジュールも分けると気せずしてマルチプロジェクト構成となる。

ここに例えばJetpack Composeを使うように設定を加えると途端に面倒くさくなる。1回ベタ書きしてみたものの、build.gradleが肥大化してとても見にくくなってしまった。

gradleの設定をComposeならComposeの設定だけ書いてまとめる。見た目的にも、設定的にもよさそうである。

そんなわけで割りと実用性に迫られて読み解きながら設定をしていった。

https://github.com/DroidKaigi/conference-app-2023/tree/main/build-logic

まずはbuild.gradleからbuild.gradle.ktsに書き換えるところがひとつの山場で、その作業にえらく時間を取られる。

後からわかったことではあるが、使う側は別にKotlinにしなくても問題なかった。Groovyのままでも利用可能である。

## 設定を使い回す

名前はComposite buildとか、Precompiled scriptとか、Convention Pluginなどと呼ばれるものらしい。それぞれ同じ概念なのか違うものなのかいまいちわかっていない。

ちょっと前まではbuildSrcを使って、プロジェクトで使うライブラリのバージョン管理をしていたが、それの拡張版と思えばいい。ローカルでGradle Pluginを作成して参照し設定を使い回せる。

ライブラリのバージョン管理に関しては、Version Catalogという仕組みがある。最近はそちらがトレンドであって、比較的新しいプロジェクトではこちらを使っている印象がある。Droidkaigiでも使っている。

Android Studioのサポートもあり、最近ではVersion Catalogを使うことに抵抗はなくなったと思う（定義元に飛べたり、コード補完が効いたりするので）。

### build-logicディレクトリの読み込み

まずはbuild-logicディレクトリをどうやって読み込んでるのかという話である。

これはrootのsetting.gradle.ktsのpluginManagerブロックにある、`includeBuild("build-logic")`で読み込みが行われている。ためしに空のフォルダを作成してそれを参照してみたが、それだけだとエラーが出る。build-logicディレクトリにsetting.gradle(.kts)とbuild.gradle(.kts)を用意したらgradle syncに成功した。

ここで注意したいのは、versionCatalogの定義が別途必要だということ。デフォルトではgradle/libs.versions.tomlファイルを用意すれば認識してくれる。しかしPrecompiled Script内ではなぜかそれが行われない。そのためsetting.gradle(.kts)でversionCatalogsをわざわざ宣言しなければならない。

https://github.com/gradle/gradle/issues/15383

### 依存関係に読み込む

新しくGradle Pluginを読み込んで自作Pluginを書くためには、まず該当のPluginを係読み込まなければならない。dependenciesに読み込むということだ。

[VersionCatalogUpdate plugin](https://github.com/littlerobots/version-catalog-update-plugin)を例にすると、まずこいつを依存関係の中に打ち込む必要がある。

普通に読み込むならpluginsブロックにidとversionを指定すればよいが、依存関係に組み込むためにはmoduleで指定する必要がある。一般的にid名はREADMEに書いてあるが、moduleの指定方法は書かれていない。

これを調べるには[Gradle Plugin Portal](https://plugins.gradle.org/)にアクセスしてid名で検索するとよい。

legacy plugin applicationのところにclasspathにかかれているのがmodule名である。

これをbuild-logic/build.gradle.ktsのdependenciesに書くことで参照できるようになるのと同時に、classpathへの組み込みと同じ結果が得られる。だからrootのbuild.gradleのpluginでわざわざ読み込みしなくても動く。

Droidkaigiのbuild-logicではlibs.versions.tomlファイルのbundleのところに追加してやればよい。pluginsのところにid名を登録する必要はない。

ここがわかりにくいポイントだったので、わかってしまえば必要ない記述を削除してすっきりさせるといい感じになる。

### Pluginを書く

次にPluginを書いていく。ここで注意したいのは、Pluginのクラスを作成するので、そのままでは`android { 設定を書いていく }`のように書くことはできない。DSLを定義することでかけるようになる。

よく見ればDSLが定義してあり、それのおかげで普段build.gradleに書くのと同じように設定が書けているのである。

DSLを書く上で必要なのは、`android {}`ブロックで何を参照しているかということ。答えはBaseAppModuleExtensionになるのだが、それの調べ方が次に問題になる。

- build.gradle.ktsにしてコード参照（cmd+クリック）で何が適用されているか調べる
- 該当のGradle Pluginのソースコードを見てXXXExtensionとなっているものを探す

上記のいずれかであるが、まあ簡単なのは前者だと思う。1度巣の状態でpluginを適用してみて、何が適用されているか調べるのが楽だろう。小規模なPluginであれば後者の方法の方が逆に早かったりする。

DSLさえわかりさえすれば、あとは自分で書くPluginの中で設定を記述していけばよい。中にはちょっと変わった書き方が必要な部分もあるが、そこまでつまることはないだろう。

### 自分で書いたPluginを参照できるようにする

自分で書いたPluginはbuild-logic/build.gradle.ktsに`register("") {}`で登録することで参照できるようになる。

```gradle
        register("versionCatalogUpdatePlugin") {
            id = "jp.gcreate.versionCatalogUpdate"
            implementationClass = "jp.gcreate.gradleshare.plugin.VersionCatalogUpdatePlugin"
        }
        // register("他とかぶらない名前") {
        //    id = "他とかぶらない名前"
        //    implementationClass = "自分で書いたPluginの完全修飾名"
        // }
```

## まとめ

自分でPrecompiled scriptを書いてみて、ようやく何がどうなって動いているのかがわかってきたように思う。

最初はまるっとコピーして動かしてみるところから始め、0から書いてみるところでハマり、ようやくここまで来たといった感じ。

サンプルとして自分でマルチモジュール構成にしたサンプルを作って公開しているので、よければそちらも参考にしてほしい。といっても、まだこちらは育てている最中なのであまり整理できてないのだけれど。

https://github.com/gen0083/MultiProjectGradleSample

## 参考

- <https://qiita.com/irgaly/items/b735b61ff73d43e8741d>
- <https://star-zero.medium.com/gradle%E3%81%AEconvention-plugins-ba19a1332540>