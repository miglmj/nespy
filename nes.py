import sys
import os

if __name__ == "__main__":
    print "Nespy: The Python NES Emulator"
    romfile = sys.argv[1]
    if romfile is None:
        print "Usage: python nes.py /path/to/rom"
    print "Loading Rom", romfile
    pass
