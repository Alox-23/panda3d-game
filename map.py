from direct.showbase.ShowBase import ShowBase
import block

class Map():
    def __init__(self, key):
        self.blocks = []
        self.node = render.attachNewNode(key)
        self.add_block()
        print(key)

    def add_block(self):
        self.blocks.append(block.Block(self.node))
