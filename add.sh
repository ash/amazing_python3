#/bin/bash

git add $1*py $1.txt
git commit -m'$1'
git push
