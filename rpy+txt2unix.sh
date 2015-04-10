#!/bin/bash

FILES=$(find $(dirname "$0") -type f -name *.rpy)
for F in $FILES; do
    tr -d '\015' < $F > temp.rpy
    mv temp.rpy $F
done

FILES=$(find $(dirname "$0") -type f -name *.txt)
for F in $FILES; do
    tr -d '\015' < $F > temp.txt
    mv temp.txt $F
done