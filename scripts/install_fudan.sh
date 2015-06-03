#!/bin/sh
FUDAN_URL="https://fudannlp.googlecode.com/files/FudanNLP-1.6.1.tar.gz"
DEST=$( cd "$( dirname "$0" )" && pwd )/../third-parties/
FUDAN=${DEST}/fudan

if [ ! -z $1 ] && [ $1 = "clean" ]; then
    rm -Rf $FUDAN
fi

if [ ! -d $FUDAN ]; then
    mkdir -p $FUDAN
    wget -O - $FUDAN_URL | tar -xz -C $FUDAN
fi
