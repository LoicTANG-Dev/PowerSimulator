from GUIDataModule import Component
class GUIGenerator(Component.Component):
    genbusPosition = {}

    def __init__(self,centerX,centerY,gid,genbusPositionX,genbusPositionY):
        super().__init__()
        self.genbusPosition = {}
        self.init(centerX,centerY)
        self.referenceInstanceGid = gid
        self.name = "Generator"
        self.genbusPosition["x"] = genbusPositionX
        self.genbusPosition["y"] = genbusPositionY