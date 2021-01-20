class GUIData():

    filePath = ''
    componentAttrs ={}
    components = {}
    clickPosition = {}
    currentSelectedComponent = None

    def __init__(self):

        self.filePath = ''
        self.componentAttrs['Bus'] = ["gid","busId","busType","pd","qd","gs","bs","busArea","vm","va","baseKv","zone","vmax","vmin"]
        self.componentAttrs['Branch'] = ["gid","fBus","tBus","brR","brX","brB","rateA",'rateB',"rateC","tap","shift","brStatus","angmin","angmax","pf","qf","pt","qt"]
        self.componentAttrs['Generator'] = ["gid","genBus","pg","qg","qmax","qmin","vg","mbase","genStatus","pmax","pmin","pc1","pc2","qc1min","qc1max","qc2min","qc2max","rampAgc","ramp10","ramp30","rampQ","apf","muPmax","muPmin","muQmax","muQmin"]
        self.componentAttrs['GeneratorCost'] = ["gid","model","startup","shutdown","ncost","cost"]
        self.componentAttrs['DCLine'] = ["gid","fBus","tBus","brStatus","pf","pt","qt","vf","vt","pmin","pmax","qminf","qmaxf","qmint","qmaxt","loss0","loss1","muPmin","muPmax","muQminf","muQmaxf","muQmint","muQmaxt"]
        self.components["Bus"] = []
        self.components["Generator"] = []
        self.components["Branch"] = []
        self.components["DCLine"] = []
        self.clickPosition["x"] = 0
        self.clickPosition["y"] = 0
        self.currentSelectedComponent = None

    def checkSelection(self,x,y):
        selected = False
        for component in self.components:
            for ele in self.components[component]:
                if x > ele.selectingArea["minX"] and x < ele.selectingArea["maxX"] and y > ele.selectingArea["minY"] and y < ele.selectingArea["maxY"]:
                    selected = True
                    self.currentSelectedComponent = ele
                    break
            if selected == True:
                break
        return selected
    
    def deleteCurrentSelectedComponent(self):
        flag = False
        if self.currentSelectedComponent != None:
            for component in self.components:
                for ele in self.components[component]:
                    if ele == self.currentSelectedComponent:
                        flag = True
                        self.components[component].remove(ele)
                        break
                if flag == True:
                    break
        self.currentSelectedComponent = None
    
    def clearCurrentSelectedComponent(self):
        self.currentSelectedComponent = None
    
    def setClickPosition(self,x,y):
        self.clickPosition["x"] = x
        self.clickPosition["y"] = y

    def clearClickPosition(self):
        self.clickPosition["x"] = 0
        self.clickPosition["y"] = 0

    def clearFilePath(self):
        self.filePath = ''
    
    def findComponentByGid(self,gid):
        find = None
        for component in self.components:
            for ele in self.components[component]:
                if ele.referenceInstanceGid == gid:
                    find = ele
                    break
            if find != None:
                break
        return find
pass

Instance = GUIData()