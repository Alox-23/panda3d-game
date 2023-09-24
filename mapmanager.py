from direct.showbase.ShowBase import ShowBase
import map

class MapManager():
    def __init__(self):
        self.maps = {}
        self.current = ""

    def add_map(self, key):
        self.maps[key] = map.Map(key)

    def set_map(self, new_key):
        if self.current == "":
            self.maps[new_key].node.reparentTo(render)
            self.current = new_key
        else:
            self.maps[self.current].node.detachNode()
            self.maps[new_key].node.reparentTo(render)
            self.current = new_key
