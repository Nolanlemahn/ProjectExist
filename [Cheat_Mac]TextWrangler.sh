#!/bin/bash
#run all cheatsheets files in TextWraongler
FILES=$(find "$(dirname "$0")/DevExtras/Cheatsheets" -type f -name *.txt)
for F in $FILES; do
    edit $F
done