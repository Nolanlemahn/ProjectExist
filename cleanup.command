#!/bin/bash
cd "$(dirname "$0")/game"
rm *.rpyc
rm debuglog.txt
echo "" > debuglog.txt
cd saves
rm *