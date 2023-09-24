from direct.showbase.ShowBase import ShowBase

class Block():
    def __init__(self, node, posx = 0, posy = 0, posz = 0):
        self.model = loader.loadModel("models/block.egg")
        self.model.reparentTo(node)
        self.texture = loader.loadTexture("img/magma.jpg")
        self.model.setTexture(self.texture)
        self.model.setPos(posx, posy, posz)
