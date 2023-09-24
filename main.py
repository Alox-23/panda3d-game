from direct.showbase.ShowBase import ShowBase
import mapmanager
import math
from direct.task import Task

class Game(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)

        self.map_manager = mapmanager.MapManager()
        self.map_manager.add_map("scene2")
        self.map_manager.set_map("scene2")
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 20.0
        angleRadians = angleDegrees * (3.14 / 180.0)
        self.camera.setPos(20 * math.sin(angleRadians), -20 * math.cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

if __name__ == "__main__":
    app = Game()
    app.run()
