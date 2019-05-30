---
title: "{{ replace .Name "-" " " | title }}"
slug: "{{ .Name }}"
date: {{ .Date }}
tags:
    - "Android Studio"
    - Kotlin
---

moreまでに入力した部分が.Summaryとして扱われる
別途descriptionを用意したい場合はfrontmatterにdescriptionを作ってそっちに書く
frontmatterのdescriptionの方が優先される

<!--more-->

##
