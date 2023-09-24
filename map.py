from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath
import stone
import magma

class Map():
    def __init__(self, key):
        self.key = key
        self.node = NodePath(self.key)
        self.load_map_keys()
        self.load_map_data()
        self.build_from_map_data()
        self.add_block(stone, 0, 0, 0)
        self.add_block(magma, 0, 0, 1)

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
        temp_row = []
        temp_z_level = []
        for i in f.read():
            if self.map_keys[i] == "new_z_level":
                temp_z_level.append(temp_row)
                temp_row = []
            elif self.map_keys[i] == "new_y_level":
                self.map_data.append(temp_z_level)
            else:
                temp_row.append(self.map_keys[i])


    def build_from_map_data(self):
        self.blocks = []
        for ynum, y in enumerate(self.map_data):
            pritn("ahh")
            for znum, z in enumerate(y):
                for xnum, x in enumerate(z):
                    if x != "air":
                        if x == "stone":
                            self.add_block(stone, xnum , ynum, xnum)
                            print("added stone")
                        if x == "magma":
                            self.add_block(magma, xnum , ynum, xnum)

    def add_block(self, blocktype, x, y, z):
        self.blocks.append(blocktype.Block(self.node, posx = x, posy = y, posz = z))
