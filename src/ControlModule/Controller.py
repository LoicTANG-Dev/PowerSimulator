from FunctionModule import PowerSimulator
from Common import Subject,Message
from GUIDataModule import GUIData

class Controller(Subject.Subject) :
    app = None
    observers = []
    readyToCreateComponent = False
    componentToCreate = None
    def __init__(self):
        self.app = PowerSimulator.Instance
        self.observers = []

    def mouseRightButtonCLicked(self,event):
        print(event.x,event.y)
        if GUIData.Instance.checkSelection(event.x,event.y) == True:
            message = Message.Message("PopRightButtonMenu")
            message.param["eventX"] = event.x_root
            message.param["eventY"] = event.y_root
            self.notifyObservers(message)

    def mouseLeftButtonClicked(self,event):
        if self.readyToCreateComponent == True:
            print(event.x,event.y)
            GUIData.Instance.setClickPosition(event.x,event.y)
            message = Message.Message("ShowComponentCreatingWin")
            if self.componentToCreate == "Bus":
                self.readyToCreateComponent = False
                message.param["type"] = "Bus"
            elif self.componentToCreate == "Branch":
                self.readyToCreateComponent = False
                message.param["type"] = "Branch"
            elif self.componentToCreate == "Generator":
                self.readyToCreateComponent = False
                message.param["type"] = "Generator"
            elif self.componentToCreate == "DCLine":
                self.readyToCreateComponent = False
                message.param["type"] = "DCLine"
            self.notifyObservers(message)
    
    def deleteCurrentSelectedComponent(self):
        self.app.deleteComponent(GUIData.Instance.currentSelectedComponent.referenceInstanceGid)
        GUIData.Instance.deleteCurrentSelectedComponent()
        self.notifyObservers(Message.Message("DataBaseUpdated"))
    
    def modifiyCurrentSelectedComponent(self):
        gid = GUIData.Instance.currentSelectedComponent.referenceInstanceGid
        component = self.app.getComponentByGid(gid)
        message = Message.Message("ShowComponentMotifyingWin")
        message.param["component"] = component
        message.param["type"] = component.name
        self.notifyObservers(message)

    def readXMLButtonClicked(self):
        self.notifyObservers(Message.Message("OpenXmlReader"))
    
    def readXmlFile(self):
        for message in self.app.createComponentFromXml(GUIData.Instance.filePath):
            if message != None:
                self.notifyObservers(message)
        self.notifyObservers(Message.Message("ReadDone"))

    def writeXMLButtonClicked(self):
        self.notifyObservers(Message.Message("OpenXmlWriter"))
    
    def writeXmlFile(self):
        self.app.createXmlFile(GUIData.Instance.filePath,GUIData.Instance.components)
        self.notifyObservers(Message.Message("CreateDone"))

    def createComponentClicked(self,component):
        self.readyToCreateComponent = True
        self.componentToCreate = component
        if component == "GeneratorCost":
            self.readyToCreateComponent = False
            message = Message.Message("ShowComponentCreatingWin")
            message.param["type"] = "GeneratorCost"
            self.notifyObservers(message)

    def confirmCreatingComponentClicked(self,component):
        self.notifyObservers(Message.Message("GetComponentValue"+component))
    
    def confirmModifyingComponentClicked(self,gid):
        message = Message.Message("GetComponentModifiedValue")
        message.param["gid"] = gid
        self.notifyObservers(message)
    
    def onComponentValueReceived(self,component,values):
        message = self.app.createComponent(component,values)
        self.notifyObservers(message)
        self.readyToCreateComponent = False
        self.componentToCreate = None

    def onModifiedComponentValueReceived(self,gid,values):
        message = self.app.modifyComponent(gid,values)
        self.notifyObservers(message)
        refreshMessage = Message.Message("FreshGUIComponent")
        refreshMessage.param["referenceInstanceGid"] = GUIData.Instance.currentSelectedComponent.referenceInstanceGid
        self.notifyObservers(refreshMessage)
        GUIData.Instance.clearCurrentSelectedComponent()

    def algoClicked(self,algo):
        self.app.run(algo)
        self.notifyObservers(Message.Message("AnalysefDone"))

    def getTempResultPath(self):
        return self.app.tempResultFile
    
    def getTempResult(self):
        return self.app.getTempResult()

    def saveResultClicked(self):
        self.notifyObservers(Message.Message("SaveResult"))

    def saveResult(self):
        self.app.saveResult(GUIData.Instance.filePath)
        self.notifyObservers(Message.Message("ResultSaveDone"))

    def onExit(self):
        self.app.deleteTempResaultFile()
        self.notifyObservers(Message.Message("DeleteTempFileDone"))
    
    def onComponentCreatingExit(self):
        self.readyToCreateComponent = False
        self.componentToCreate = None
        self.notifyObservers(Message.Message("CloseComponentCreatingWin"))

    def onComponentModifyingExit(self):
        GUIData.Instance.clearCurrentSelectedComponent()
        self.notifyObservers(Message.Message("CloseComponentModifyingWin"))
    
    def onDestroyComponentCreatingWin(self):
        self.notifyObservers(Message.Message("RemoveObserverComponentCreatingWin"))

    def onDestroyComponentModifyingWin(self):
        self.notifyObservers(Message.Message("RemoveObserverComponentModifyingWin"))

    def registerObserver(self,observer):
        self.observers.append(observer)
    
    def notifyObservers(self,info):
        for item in self.observers:
            item.listen(info)
    
    def removeObserver(self,observer):
        self.observers.pop()
pass

Instance = Controller()