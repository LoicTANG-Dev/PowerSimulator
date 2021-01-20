import json

class Generator() :

    name = "Generator"
    gid = 0
    genBus = 0
    pg = 0
    qg = 0
    qmax = 0
    qmin = 0
    vg = 0
    mbase = 0
    genStatus = 0
    pmax = 0
    pmin = 0
    pc1 = 0
    pc2 = 0
    qc1min = 0
    qc1max = 0
    qc2min = 0
    qc2max = 0
    rampAgc = 0
    ramp10 = 0
    ramp30 = 0
    rampQ = 0
    apf = 0
    muPmax = 0
    muPmin = 0
    muQmax = 0
    muQmin = 0

    def __init__(self):
        self.gid = 0
        self.genBus = 0
        self.pg = 0
        self.qg = 0
        self.qmax = 0
        self.qmin = 0
        self.vg = 0
        self.mbase = 0
        self.genStatus = 0
        self.pmax = 0
        self.pmin = 0
        self.pc1 = 0
        self.pc2 = 0
        self.qc1min = 0
        self.qc1max = 0
        self.qc2min = 0
        self.qc2max = 0
        self.rampAgc = 0
        self.ramp10 = 0
        self.ramp30 = 0
        self.rampQ = 0
        self.apf = 0
        #self.muPmax = 0
        #self.muPmin = 0
        #self.muQmax = 0
        #self.muQmin = 0

    def showParam(self):
        param = json.dumps(self,default=lambda obj: obj.__dict__, sort_keys= True,indent=4)
        print("Generator: "+param)

pass

        
        