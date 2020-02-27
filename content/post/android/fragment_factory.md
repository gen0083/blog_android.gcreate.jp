---
title: "FragmentFactoryを使ってコンストラクタ経由でFragmentに値を渡す"
slug: "fragment_factory"
date: 2020-02-27T20:31:57+09:00
tags:
    - Android
    - Fragment
---

Fragmentに値を渡す場合は、Bundle経由で渡すのが常識だった。Fragmentはシステムで生成されるため、引数付きのコンストラクタが認識されなかったからだ。

しかし最近ではFragmentFactoryを使うことで、Fragmentに引数付きのコンストラクタを定義しても大丈夫になったということで、今回試してみることにした。

<!--more-->

## 今回のコード

全コードは[GitHub](https://github.com/gen0083/FragmentConstructorSample)にある。

Activityにあるボタンを押すことで、カウンターをインクリメント・デクリメントして、そのカウンターの値を引数としてFragmentを生成するというサンプルだ。

例としてはあんまりよろしくないと思う。今回のサンプルコードのようなものであれば、ActivityのViewModelをFragmentから参照すれば解決するし、そうした方がコードとしてはスッキリするはずである。

## ポイント

1. FragmentFactoryを継承したクラスを用意し、依存性を解決する
2. Activityの`super.onCreate()`を呼び出す前に`supportFragmentManager.fragmentFactory`でカスタムFactoryをセットする

重要なのは2番目だろう。`super.onCreate()`の後でファクトリをセットするとActivityの再生成時にFragmentのコンストラクタ呼び出しに失敗してアプリが落ちた。

```
class HasArgumentsFragmentFactory(val dep: () -> Int) : FragmentFactory() {
    override fun instantiate(classLoader: ClassLoader, className: String): Fragment {
        if (className == HasArgumentsFragment::class.java.name) {
            return HasArgumentsFragment(dep())
        }
        return super.instantiate(classLoader, className)
    }
}
```

Factoryでは必要なFragmentのインスタンスを返すようにすればよい。今回はカウンタの値をFragmentに渡したいので、現在のカウンタを返すlambda式をFactoryに渡している[^1]。

```
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private val vm: MainViewModel by viewModels { ViewModelProvider.NewInstanceFactory() }
    private val fragmentFactory = HasArgumentsFragmentFactory { vm.countLiveData.value ?: 0 }

    override fun onCreate(savedInstanceState: Bundle?) {
        supportFragmentManager.fragmentFactory = fragmentFactory
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)

        binding.increment.setOnClickListener {
            vm.increment()
        }
        binding.decrement.setOnClickListener {
            vm.decrement()
        }
        vm.countLiveData.observe(this, Observer {
            supportFragmentManager.beginTransaction()
                .replace(R.id.container_2, HasArgumentsFragment::class.java, null)
                .commit()
        })
    }
}
```

Activityでは`super.onCreate()`を呼び出す前にFragmentFactoryをセットしている。順番を変えたらどうなるかというと、先に述べたとおり画面回転などでアプリが落ちる。

## 実際に使うか

これまた難しい。

例えばDagger2を使うのであれば、Fragmentはフィールドインジェクションで依存性を注入することになるだろうから、わざわざコンストラクタでやる必要があるのかと思える。

ただFragmentに関するDagger2の設定をFragmentFactoryに任せられるのはいいのかもしれない。一方で`supportFragmentManager.fragmentFactory`のセットをする必要が生じるので、これを忘れてアプリが落ちるという罠にはまりそうな気がする。

もっとも私はDaggerについては復習をしないとよく分からん状態になっているので、完全にイメージというか印象だけでものを言っているので参考にならない。実際のところはどうなんだろうか。

Daggerで`inject`呼び出すのを忘れるのを回避できていいのかなと思ったが、`DispatchAndroidInjector`を使えば回避できるようだ。

Daggerの復習がてら、あらためてFragmentのコンストラクタインジェクションも試してみるとしよう。

[^1]: これなら別にFragmentのコンストラクタでやらなくても実現できるので、例としてはあまりよくない気がしている。
