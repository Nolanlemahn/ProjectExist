#!/bin/bash
cd "$(dirname "$0")/game"
rm *.rpyc
cd ..
rm debuglog.txt
rm debuglog2.txt
echo "" > debuglog.txt
echo "" > debuglog2.txt
cd game
cd saves
rm *