#!/bin/bash
BOOTSEARCH="Adafruit Feather RP2040"
# try and avoid installing on the wrong CIRCUITPY board
if grep -q "${BOOTSEARCH}" /Volumes/CIRCUITPY/boot_out.txt; then
    echo $BOOTSEARCH found on CIRCUITPY
else
    echo $BOOTSEARCH not found
    exit;
fi
# when going from 6 to 7 the mpy were out of date and I had to
#rm -rf /Volumes/CIRCUITPY/lib/*
# maybe just do that all the time anyway?
circup install -r board_requirements.txt
# install the code and the deps
cp -X boot.py /Volumes/CIRCUITPY/boot.py
cp -X code.py /Volumes/CIRCUITPY/code.py
