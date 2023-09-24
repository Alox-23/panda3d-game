from direct.showbase.ShowBase import ShowBase

class Block():
    def __init__(self, node, posx = 0, posy = 10, posz = 0):
        self.model = loader.loadModel("models/block.egg")
        self.model.reparentTo(node)
        self.texture = loader.loadTexture("img/texture.jpg")
        self.model.setTexture(self.texture)
        self.model.setPos(posx, posy, posz)
