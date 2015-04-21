#!/bin/bash
#run all rpy files in sublime
FILES=$(find $(dirname "$0") -type f -name *.rpy)
for F in $FILES; do
    subl -a $F
done