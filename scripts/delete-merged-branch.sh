#!/bin/sh

# refer: https://gist.github.com/miukoba/fc3c10a25c1c675c1e97

git fetch origin master:master
git checkout master
git branch --merged master | grep -vE '^\*|\<master\>' | xargs -I % git branch -d %
git branch -r --merged master | grep -vE '\<master\>' | sed -e 's% *origin/%%' | xargs -I% git push --delete origin %
git fetch --prune
