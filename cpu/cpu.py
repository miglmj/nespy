import numpy.uint8 as byte
import numpy.uint16 as uint16

class NESCpu:
    def __init__(self):
        #Initialize Registers
        self.registers.A = byte(0)
        self.registers.X = byte(0)
        self.registers.Y = byte(0)
        self.registers.P = byte(0)
        self.registers.SP = byte(0)
        self.registers.PC = uint16(0)

