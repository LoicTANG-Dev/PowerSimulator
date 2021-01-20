from GUIDataModule import Component
class GUIBus(Component.Component):

    def __init__(self,centerX,centerY,gid):
        super().__init__()
        self.init(centerX,centerY)
        self.referenceInstanceGid = gid
        self.name = "Bus"
        self.selectingArea["minX"] = centerX-2
        self.selectingArea["maxX"] = centerX+2
        self.selectingArea["minY"] = centerY-30
        self.selectingArea['maxY'] = centerY+30