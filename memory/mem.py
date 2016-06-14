import numpy

class NESMemory:
    def __init__(self):
        # Allocate space for memory
        self.memory = [numpy.uint8(0)] * 65536 # Entire address space
    def reset(self):
        # Reset all memory values to 0
        self.memory = [numpy.uint8(0)] * 65536
    def fetch(address):
        """
        Return value at given memory address
        TODO: Implement detecting memory ranges to account
        for mirrored memory, memory mapped to PPU/APU/Cartridge
        """
        return self.memory[address]
    def store(address, value):
        """
        Write data to given address
        Return old value at memory location
        TODO: Implement detecting memory ranges to account
        for mirrored memory, memory mapped to PPU/APU/Cartridge
        """
        oldval = self.memory[address]
        self.memory[address] = value
        return oldval
