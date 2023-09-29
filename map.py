from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath
import block

class Map():
    def __init__(self, key):
        self.key = key
        self.node = NodePath(self.key)
        self.load_map_keys()
        self.load_map_data()
        self.build_from_map_data()

    def load_map_keys(self):
        self.map_keys = {"\n" : "new_z_level"}
        f = open(f"data/keys.txt")
        key = ""
        value = ""
        value_done = False
        for i in f.read():
            if i != "\n":
                if i == ";":
                    self.map_keys[key] = value
                    value = ""
                    key = ""
                    value_done = False

                if value_done == True:
                    key += i

                if i == ":":
                    value_done = True

                if i != ":" and value_done == False and i != ";":
                    value += i                
            

    def load_map_data(self):
        self.map_data = []
        f = open(f"data/{self.key}.txt")
        temp_x = []
        temp_z = []
        temp_y = []
        for i in f.read():
            if self.map_keys[i] == "new_z_level":
                temp_z.append(temp_x)
                temp_x = []
            elif self.map_keys[i] == "new_y_level":
                temp_y.append(temp_z)
                temp_z = []
            else:
                temp_x.append(i)
        self.map_data = temp_y

    def build_from_map_data(self):
        self.blocks = []
        for ynum, y in enumerate(self.map_data):
            for znum, z in enumerate(y):
                for xnum, x in enumerate(z):
                    if self.map_keys[x] != "air":
                        self.add_block(self.map_keys[x], xnum, znum, ynum)

    def add_block(self, blocktype, x, y, z):
        self.blocks.append(block.Block(self.node, block_type = blocktype, posx = x, posy = y, posz = z))

    def get_node(self):
        return self.node
