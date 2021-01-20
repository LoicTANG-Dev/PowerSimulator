import os,shutil
import datetime
from DataModule import DataBase, ComponentFactoty
from FunctionModule import XmlReader,XmlWriter
from FunctionModule import ExtensionMethod
from pypower import rundcpf
from Common import Message

class PowerSimulator:
    tempFolder = ""
    tempResultFile = ""
    outputFolder = ""
    xmlReader = None
    xmlWriter = None

    def __init__(self):
        self.xmlReader = None
        self.xmlWriter = None

        fatherPath = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".")
        self.tempFolder = fatherPath+'\\'+"src"+'\\'+"temp"+'\\'
        self.tempResultFile = self.tempFolder + "temp.txt"
        self.outputFolder =  fatherPath+'\\'+"src"+'\\'+"Output"+'\\'

    def createComponentFromXml(self,path):
        self.xmlReader = XmlReader.XmlReader(path)

        for componentNode in self.xmlReader.getXmlContext():
            yield ComponentFactoty.Instance.createComponent(True,componentNode)

        self.xmlReader = None
    
    def checkDB(self):
        DataBase.Instance.showComponents()
    
    def createXmlFile(self,path,guiComponents):
        self.xmlWriter =  XmlWriter.XmlWriter()
        self.xmlWriter.createXMLFile(path,guiComponents)
    
    def getComponentByGid(self,gid):
        return DataBase.Instance.findComponentByGid(gid)

    def deleteComponent(self,gid):
        DataBase.Instance.deleteComponent(gid)

    def getTempResult(self):
        return ExtensionMethod.Instance.getTempResult(self.tempResultFile)

    def saveResult(self,path):
        ExtensionMethod.Instance.saveResult(self.tempResultFile,path)

    def deleteTempResaultFile(self):
        ExtensionMethod.Instance.deleteTempResaultFile(self.tempResultFile)
    
    def createComponent(self,component,values):
        return ComponentFactoty.Instance.createComponent(False,(component,values))
    
    def modifyComponent(self,gid,values):
        componentToModify = DataBase.Instance.findComponentByGid(gid)
        ComponentFactoty.Instance.setComponentParam(componentToModify,values)
        return Message.Message("ComponentModifiedDone")
        

    def run(self,algo):
        case = ExtensionMethod.Instance.convertDataToCase()
        rundcpf.rundcpf(case,None,self.tempResultFile)


Instance = PowerSimulator()