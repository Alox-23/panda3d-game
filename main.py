from direct.showbase.ShowBase import ShowBase
import mapmanager

class Game(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)
        self.map_manager = mapmanager.MapManager()
        self.map_manager.add_map("scene1")
        self.map_manager.add_map("scene2")
        self.map_manager.set_map("scene1")

if __name__ == "__main__":
    app = Game()
    app.run()
