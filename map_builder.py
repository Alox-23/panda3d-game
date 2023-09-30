from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import math
from direct.task import Task
from panda3d.core import NodePath
import block


class MapManager():
    def __init__(self):
        self.maps = {}
        self.current = ""

    def add_map(self, key):
        self.maps[key] = Map(key)

    def set_map(self, new_key):
        if self.current == "":
            self.maps[new_key].node.reparentTo(render)
            self.current = new_key
        else:
            self.maps[self.current].node.detachNode()
            self.maps[new_key].node.reparentTo(render)
            self.current = new_key

    def get_current_node(self):
        return self.maps[self.current].get_node()



class Map():
    def __init__(self, key):
        self.key = key
        self.node = NodePath(self.key)
        self.load_map_keys()
        taskMgr.add(self.reload, "reload_map")

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
        f = data
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

    def reload(self, task):
        self.node.removeAllChildren()
        self.load_map_data()
        self.build_from_map_data()
        return task.cont



class Game(ShowBase):
    
    def __init__(self): 
        while True:
            #self.map_path = input("Which map do you want to edit?")
            self.map_path = "scene2.txt"
            global data
            try:
                data = open(f"data/{self.map_path}")
                break
            except:
                print("invalid map name")
                continue

        ShowBase.__init__(self)
        self.map_manager = MapManager()
        self.map_manager.add_map(self.map_path)
        self.map_manager.set_map(self.map_path)
        taskMgr.add(self.load_data, "data_load")

        self.disableMouse()

        self.accept("w", self.__key, ["w"])
        self.accept("a", self.__key, ["a"])
        self.accept("s", self.__key, ["s"])
        self.accept("d", self.__key, ["d"])
        self.accept("r", self.__key, ["r"])
        self.accept("f", self.__key, ["f"])
        self.accept("arrow_left", self.__key, ["left"])
        self.accept("arrow_right", self.__key, ["right"])
        self.accept("arrow_up", self.__key, ["up"])
        self.accept("arrow_down", self.__key, ["down"])

    def __key(self, key):
        if key == "w":
            self.camera.setY(self.camera, 2)
        elif key == "a":
            self.camera.setX(self.camera, -2)
        elif key == "s":
            self.camera.setY(self.camera, -2)
        elif key == "r":
            self.camera.setZ(self.camera, 2)
        elif key == "f":
            self.camera.setZ(self.camera, -2)

        elif key == "d":
            self.camera.setX(self.camera, 2)
        elif key == "left":
            self.camera.setH(self.camera, 4)
        elif key == "right":
            self.camera.setH(self.camera, -4)
        elif key == "up":
            self.camera.setP(self.camera, 4)
        elif key == "down":
            self.camera.setP(self.camera, -4)


    def load_data(self, task):
        data = open(f"data/{self.map_path}")
        return task.cont
 
if __name__ == "__main__":
    app = Game()
    app.run()
