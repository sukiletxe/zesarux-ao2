#!/bin/bash
VERSION=`cat ../src/version.txt`
TEXTO=`cat`

python speech_filters/zesarux-ao2-$VERSION/src/main.py "$TEXTO"
