#!/bin/bash

clear

# style=vs
pygmentize -f terminal256 -O style=monokai -g $1.py
screencapture -l $(osascript -e 'tell app "Terminal" to id of window 1') $1-temp.png
convert $1-temp.png[600x600+114+114] $1.png
rm $1-temp.png

clear
echo "$ python3 $1.py"
python3 $1.py
echo "$ "
screencapture -l $(osascript -e 'tell app "Terminal" to id of window 1') $1-temp.png
convert $1-temp.png[600x600+114+114] $1.out.png
rm $1-temp.png

