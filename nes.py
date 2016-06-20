import sys
import os
from cart import Cartridge

class Nes(Object):

    def __init__(self):
        #initialize internal components
        pass

    def insert_cart(self, data):
        self.cartridge = Cartridge(data)


if __name__ == "__main__":
    print ("Nespy: The Python NES Emulator")
    romfile = sys.argv[1]
    if romfile is None:
        print ("Usage: python nes.py /path/to/rom")
    print ("Loading Rom file: ", romfile)

    with open(romfile, 'rb') as rom:
        data = rom.readlines()

    nes = Nes()

    nes.insert_cart(data)
