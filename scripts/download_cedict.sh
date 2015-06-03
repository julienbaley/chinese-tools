#!/bin/sh
CEDICT_URL="http://cc-cedict.org/editor/editor_export_cedict.php?c=gz"
#DEST=$(cd $(dirname "$BASH_SOURCE"); pwd)/../data/
DEST=$( cd "$( dirname "$0" )" && pwd )/../data
mkdir -p $DEST
wget -O - $CEDICT_URL | zcat > ${DEST}/cedict.txt   #decompress to destination
