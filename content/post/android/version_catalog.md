---
title: "versionCatalogsを使った依存関係の管理"
slug: "version_catalog"
date: 2022-06-21T16:24:06+09:00
tags:
    - "Android Studio"
    - Kotlin
    - Gradle
---

Gradleの機能として提供されているversionCatalogsを使って依存関係を定義してみた。

<!--more-->

Gradle7.3.3ではfeature previewのため、setting.gradleで`enableFeaturePreview('VERSION_CATALOGS')`を指定しないと動かない。Gradle7.4.2以降は不要。

tomlファイルに依存関係を定義して読み込めるのが特徴。複数のプロジェクトで1つのファイルを使い回せたりする。

ファイルの位置や名前は設定で指定できるが、デフォルトではgradleディレクトリ配下にlibs.versions.tomlという名前のファイルを用意することで自動的に読み込まれる。

tomlファイル内ではハイフンを使った表記で指定しても動くが、基本的にハイフンは`.`に置き換えられる。例えば`androidx-core`と別名をつけた場合、`adroidx.core`に置き換えられる。

便利なのはbundleで複数のライブラリを一気に指定できることだろう。例えばlifecycleを1つにまとめて指定できる。

```
dependencies {
        def lifecycle_version = "2.5.0-rc02"
        def arch_version = "2.1.0"

        // ViewModel
        implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version"
        // ViewModel utilities for Compose
        implementation "androidx.lifecycle:lifecycle-viewmodel-compose:$lifecycle_version"
        // LiveData
        implementation "androidx.lifecycle:lifecycle-livedata-ktx:$lifecycle_version"
        // Lifecycles only (without ViewModel or LiveData)
        implementation "androidx.lifecycle:lifecycle-runtime-ktx:$lifecycle_version"

        // Saved state module for ViewModel
        implementation "androidx.lifecycle:lifecycle-viewmodel-savedstate:$lifecycle_version"

        // Annotation processor
        kapt "androidx.lifecycle:lifecycle-compiler:$lifecycle_version"
        // alternately - if using Java8, use the following instead of lifecycle-compiler
        implementation "androidx.lifecycle:lifecycle-common-java8:$lifecycle_version"

        // optional - helpers for implementing LifecycleOwner in a Service
        implementation "androidx.lifecycle:lifecycle-service:$lifecycle_version"

        // optional - ProcessLifecycleOwner provides a lifecycle for the whole application process
        implementation "androidx.lifecycle:lifecycle-process:$lifecycle_version"

        // optional - ReactiveStreams support for LiveData
        implementation "androidx.lifecycle:lifecycle-reactivestreams-ktx:$lifecycle_version"

        // optional - Test helpers for LiveData
        testImplementation "androidx.arch.core:core-testing:$arch_version"
    }
```

これをtomlファイルで次のように定義する[^1]。

```
[versions]
android-plugin = "7.2.0"
kotlin = "1.6.21"
lifecycle = "2.5.0-rc02"
arch = "2.1.0"

[libraries]
androidx-lifecycle-viewmodel = { module = "androidx.lifecycle:lifecycle-viewmodel-ktx", version.ref = "lifecycle" }
androidx-lifecycle-viewmodel-compose = { module = "androidx.lifecycle:lifecycle-viewmodel-compose", version.ref = "lifecycle" }
androidx-lifecycle-livedata = { module = "androidx.lifecycle:lifecycle-livedata-ktx", version.ref = "lifecycle" }
androidx-lifecycle-viewmodel-savestate = { module = "androidx.lifecycle:lifecycle-viewmodel-savedstate", version.ref = "lifecycle" }
androidx-lifecycle-compiler = { module = "androidx.lifecycle:lifecycle-compiler", version.ref = "lifecycle" }
androidx-lifecycle-common-java8 = { module = "androidx.lifecycle:lifecycle-common-java8", version.ref = "lifecycle" }
androidx-lifecycle-service = { module = "androidx.lifecycle:lifecycle-service", version.ref = "lifecycle" }
androidx-lifecycle-process = { module = "androidx.lifecycle:lifecycle-process", version.ref = "lifecycle" }
androidx-lifecycle-reactivestreams = { module = "androidx.lifecycle:lifecycle-reactivestreams-ktx", version.ref = "lifecycle" }
androidx-core-testing = { module = "androidx.arch.core:core-testing", version.ref = "arch" }

[bundles]
lifecycle = [
    "androidx.lifecycle.viewmodel",
    "androidx-lifecycle-viewmodel-compose",
    "androidx-lifecycle-livedata",
    "androidx.lifecycle.viewmodel.savestate",
    "androidx.lifecycle.common.java8",
    "androidx.lifecycle.service",
    "androidx.lifecycle.process",
    "androidx.lifecycle.reactivestreams"
]

[plugins]
android-application = { id = 'com.android.application', version.ref = 'android.plugin' }
android-library = { id = 'com.android.library', version.ref = 'android.plugin' }
kotlin-android = { id = 'org.jetbrains.kotlin.android', version.ref = 'kotlin' }
```

app/build.gradleのdependenciesブロックで`implementation libs.bundles.lifecycle`と定義すればまとめて依存関係がインストールされる。便利。

このファイルを共有すれば複数のプロジェクトでいちいち依存関係を調べる作業から開放される。

ただし現時点ではIDEのサポートが一切受けられない。動作に問題はないが、どうせならコード補完で指定できたり、定義箇所に飛んだりする機能があるとより便利になるだろう。今後に期待。

https://docs.gradle.org/current/userguide/platforms.html

[^1]: ハイフンと`.`が混ざっているのは、ファイル内でどちらの定義でも動くことを確認するため、わざとやっている。