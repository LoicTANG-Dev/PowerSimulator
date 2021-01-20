from GUIDataModule import GUIData
from DataModule import DataBase,Branch,Bus,Generator,DCLine
from GUIDataModule import GUIBus,GUIGenerator,GUIBranch,GUIDCLine
from Common import Message

class GUIComponentFactory():
    
    def __init__(self):
        return
    
    def createBus(self,gid,fromXML,centerX=0,centerY=0):
        if fromXML == True:
            bus = GUIBus.GUIBus(centerX,centerY,gid)
        else:
            bus = GUIBus.GUIBus(GUIData.Instance.clickPosition["x"],GUIData.Instance.clickPosition["y"],gid)
        GUIData.Instance.components["Bus"].append(bus)
    
    def createGenerator(self,gid,fromXML,centerX=0,centerY=0):
        genbus = GUIData.Instance.findComponentByGid(DataBase.Instance.findBusById(DataBase.Instance.findComponentByGid(gid).genBus).gid)
        if fromXML == True:
            generator = GUIGenerator.GUIGenerator(centerX,centerY,gid,genbus.centerPosition["x"],genbus.centerPosition["y"])
        else:
            generator = GUIGenerator.GUIGenerator(GUIData.Instance.clickPosition["x"],GUIData.Instance.clickPosition["y"],gid,genbus.centerPosition["x"],genbus.centerPosition["y"])
        GUIData.Instance.components["Generator"].append(generator)

    def createBranch(self,gid,fromXML,centerX=0,centerY=0):
        fBus = GUIData.Instance.findComponentByGid(DataBase.Instance.findBusById(DataBase.Instance.findComponentByGid(gid).fBus).gid)
        tBus = GUIData.Instance.findComponentByGid(DataBase.Instance.findBusById(DataBase.Instance.findComponentByGid(gid).tBus).gid)
        if fromXML == True:
            branch = GUIBranch.GUIBranch(centerX,centerY,gid,fBus.centerPosition["x"],fBus.centerPosition["y"],tBus.centerPosition["x"],tBus.centerPosition["y"])
        else:
            branch = GUIBranch.GUIBranch(GUIData.Instance.clickPosition["x"],GUIData.Instance.clickPosition["y"],gid,fBus.centerPosition["x"],fBus.centerPosition["y"],tBus.centerPosition["x"],tBus.centerPosition["y"])
        GUIData.Instance.components["Branch"].append(branch)

    def createDCLine(self,gid,fromXML,centerX=0,centerY=0):
        fBus = GUIData.Instance.findComponentByGid(DataBase.Instance.findBusById(DataBase.Instance.findComponentByGid(gid).fBus).gid)
        tBus = GUIData.Instance.findComponentByGid(DataBase.Instance.findBusById(DataBase.Instance.findComponentByGid(gid).tBus).gid)
        if fromXML == True:
            dcline = GUIDCLine.GUIDCLine(centerX,centerY,gid,fBus.centerPosition["x"],fBus.centerPosition["y"],tBus.centerPosition["x"],tBus.centerPosition["y"])
        else:
            dcline = GUIDCLine.GUIDCLine(GUIData.Instance.clickPosition["x"],GUIData.Instance.clickPosition["y"],gid,fBus.centerPosition["x"],fBus.centerPosition["y"],tBus.centerPosition["x"],tBus.centerPosition["y"])
        GUIData.Instance.components["DCLine"].append(dcline)

    def createComponent(self,component,gid,fromXML,centerX=0,centerY=0):
        if component == "Bus":
            if fromXML == True:
                self.createBus(gid,fromXML,centerX,centerY)
            else:
                self.createBus(gid,fromXML)
        elif component == "Generator":
            if fromXML == True:
                self.createGenerator(gid,fromXML,centerX,centerY)
            else:
                self.createGenerator(gid,fromXML)
        elif component == "Branch":
            if fromXML == True:
                self.createBranch(gid,fromXML,centerX,centerY)
            else:
                self.createBranch(gid,fromXML)
        elif component == "DCLine":
            if fromXML == True:
                self.createDCLine(gid,fromXML,centerX,centerY)
            else:
                self.createDCLine(gid,fromXML)

    def refreshGUIComponent(self,gid):
        component = GUIData.Instance.findComponentByGid(gid)
        if component.name == "Bus":
            self.createBus(gid,True,component.centerPosition["x"],component.centerPosition["y"])
        elif component.name == "Generator":
            self.createGenerator(gid,True,component.centerPosition["x"],component.centerPosition["y"])
        elif component.name == "Branch":
            self.createBranch(gid,True,component.centerPosition["x"],component.centerPosition["y"])
        elif component.name == "DCLine":
            self.createDCLine(gid,True,component.centerPosition["x"],component.centerPosition["y"])
        GUIData.Instance.deleteCurrentSelectedComponent()

Instance = GUIComponentFactory()