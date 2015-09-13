#!/bin/bash
VERSION=`cat ../src/version.txt`
TEXTO=`cat`

python zesarux-ao2-$VERSION/src/main.py "$TEXTO"
