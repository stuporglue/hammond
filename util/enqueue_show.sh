#!/bin/bash

hammy=$(pgrep -f python3.*hammond.py)
exitcode=$?

if [ $exitcode -eq 0 ]; then
	kill -s usr1 $hammy
else
	beep -f 300 -n -f 100 -l 400
fi
