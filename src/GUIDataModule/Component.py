class Component:
    centerPosition = {}
    selectingArea = {}
    referenceInstanceGid = ""
    name = ""

    def __init__(self):
        self.centerPosition = {}
        self.selectingArea = {}
        self.referenceInstanceGid = ""
        self.name = ""
    
    def init(self,centerX,centerY):
        self.centerPosition["x"] = centerX
        self.centerPosition["y"] = centerY
        self.selectingArea["minX"] = centerX-10
        self.selectingArea["maxX"] = centerX+10
        self.selectingArea["minY"] = centerY-10
        self.selectingArea['maxY'] = centerY+10
    
    def setCenterPosition(self,centerX,centerY):
        self.init(centerX,centerY)