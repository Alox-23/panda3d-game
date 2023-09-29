from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import mapmanager
import math
from direct.task import Task

class Game(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)

        self.map_manager = mapmanager.MapManager()
        self.map_manager.add_map("scene2")
        self.map_manager.set_map("scene2")
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



if __name__ == "__main__":
    app = Game()
    app.run()
