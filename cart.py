class Cartridge(Object):
    def __init__(self, data):
        if is_NES_game(data):
            self.data = data

def is_NES_game(data):
    if data[0][0:3] != b'NES':
        print ("INVALID ROM FILE")
        return False
    else:
        print("Valid NES Game")
        return True
