import json

class Branch():

    name = "Branch"
    gid = 0
    fBus = 0
    tBus = 0
    brR = 0
    brX = 0
    brB = 0
    rateA = 0
    rateB = 0
    rateC = 0
    tap = 0
    shift = 0
    brStatus = 0
    angmin = 0
    angmax = 0
    pf = 0
    qf = 0
    pt = 0
    qt = 0
    #muSf = 0
    #muSt = 0
    #muAngmin = 0
    #muAngmax = 0

    def __init__(self):
        self.gid = 0
        self.fBus = 0
        self.tBus = 0
        self.brR = 0
        self.brX = 0
        self.brB = 0
        self.rateA = 0
        self.rateB = 0
        self.rateC = 0
        self.tap = 0
        self.shift = 0
        self.brStatus= 0
        self.angmin= 0
        self.angmax = 0
        self.pf = 0
        self.qf = 0
        self.pt = 0
        self.qt = 0
        #self.muSf = 0
        #self.muSt = 0
        #self.muAngmin = 0
        #self.muAngmax = 0

    def showParam(self):
        param = json.dumps(self,default=lambda obj: obj.__dict__, sort_keys= True,indent=4)
        print("Branch: "+param)

pass
