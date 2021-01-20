from GUIDataModule import Component
class GUIBranch(Component.Component):
    fbusPosition = {}
    tbusPosition = {}
    def __init__(self,centerX,centerY,gid,fbusPositionX,fbusPositionY,tbusPositionX,tbusPositionY):
        super().__init__()
        self.fbusPosition = {}
        self.tbusPosition = {}
        self.init(centerX,centerY)
        self.referenceInstanceGid = gid
        self.name = "Branch"
        if tbusPositionX < fbusPositionX:
            self.fbusPosition["x"] = tbusPositionX
            self.fbusPosition["y"] = tbusPositionY
            self.tbusPosition["x"] = fbusPositionX
            self.tbusPosition["y"] = fbusPositionY
        else:
            self.fbusPosition["x"] = fbusPositionX
            self.fbusPosition["y"] = fbusPositionY
            self.tbusPosition["x"] = tbusPositionX
            self.tbusPosition["y"] = tbusPositionY