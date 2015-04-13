cd game
del *.rpyc
cd ..
del debuglog.txt
del debuglog2.txt
type NUL > debuglog.txt
type NUL > debuglog2.txt
::THE TYPE COMMAND IS NOT YET TESTED
cd saves
del /Q *