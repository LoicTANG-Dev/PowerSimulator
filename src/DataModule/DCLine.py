import json

class DCLine():

    name = "DCLine"
    gid = 0
    fBus = 0
    tBus = 0
    brStatus = 0
    pf = 0
    pt = 0
    qt = 0
    vf = 0
    vt = 0
    pmin = 0
    pmax = 0
    qminf = 0
    qmaxf = 0
    qmint = 0
    qmaxt = 0
    loss0 = 0
    loss1 = 0
    muPmin = 0
    muPmax = 0
    muQminf = 0
    muQmaxf = 0
    muQmint = 0
    muQmaxt = 0

    def __init__(self):
        self.gid = 0
        self.fBus = 0
        self.tBus = 0
        self.brStatus= 0
        self.pf = 0
        self.pt = 0
        self.qt = 0
        self.vf = 0
        self. vt = 0
        self.pmin = 0
        self.pmax = 0
        self.qminf = 0
        self.qmaxf = 0
        self.qmint = 0
        self.qmaxt = 0
        self.loss0 = 0
        self.loss1 = 0
        self.muPmin = 0
        self.muPmax = 0
        self.muQminf = 0
        self.muQmaxf = 0
        self.muQmint = 0
        self.muQmaxt = 0

    def init(self, DCLineId, fBus, tBus, brStatus, pf, pt, qt, vf, vt, pmin, pmax, qminf, qmaxf, qmint, qmaxt, loss0, loss1, muPmin, muPmax, muQminf, muQmaxf, muQmint, muQmaxt):
        self.DCLineId = DCLineId
        self.fBus = fBus
        self.tBus = tBus
        self.brStatus = brStatus
        self.pf = pf
        self.pt = pt
        self.qt = qt
        self.vf = vf
        self.vt = vt
        self.pmin = pmin
        self.pmax = pmax
        self.qminf = qminf
        self.qmaxf = qmaxf
        self.qmint = qmint
        self.qmaxt = qmaxt
        self.loss0 = loss0
        self.loss1 = loss1
        self.muPmin = muPmin
        self.muPmax = muPmax
        self.muQminf = muQminf
        self.muQmaxf = muQmaxf
        self.muQmint = muQmint
        self.muQmaxt = muQmaxt

    def showParam(self):
        param = json.dumps(self,default=lambda obj: obj.__dict__, sort_keys= True,indent=4)
        print("DCLine: "+param)

pass
     
