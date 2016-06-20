import sys
import os

if __name__ == "__main__":
    print "Nespy: The Python NES Emulator"
    romfile = sys.argv[1]
    if romfile is None:
        print "Usage: python nes.py /path/to/rom"
    print "Loading Rom file: ", romfile

    with open(romfile, 'rb') as rom:
        data = rom.readlines()

    print "Read", len(data), "lines from ROM file"

    if data[0][0:3] != "NES":
        print "INVALID ROM FILE"
    else:
        print "Valid NES Game"
