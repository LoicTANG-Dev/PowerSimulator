import json

class Bus():

    name = "Bus"
    gid = 0
    busId = 0
    busType = 0
    pd = 0
    qd = 0
    gs = 0
    bs = 0
    busArea = 0
    vm = 0
    va = 0
    baseKv = 0
    zone = 0
    vmax = 0
    vmin = 0
    #lamP = 0
    #lamQ = 0
    #muVmax = 0
    #muVmin = 0 


    def __init__(self):
        self.gid = 0
        self.busId = 0
        self.busType = 0
        self.pd = 0
        self.qd = 0
        self.gs = 0
        self.bs = 0
        self.busArea = 0
        self.vm = 0
        self.va = 0
        self.baseKv = 0
        self.zone = 0
        self.vmax = 0
        self.vmin = 0
        #self.lamP = 0
        #self.lamQ = 0
        #self.muVmax = 0
        #self.muVmin = 0

    def showParam(self):
        param = json.dumps(self,default=lambda obj: obj.__dict__, sort_keys= True,indent=4)
        print("Bus: "+param)


pass
