from DataModule import DataBase
from numpy import array
import os,datetime,shutil

class ExtensionMethod:

    def __init__(self):
        return
    
    def getTempResult(self,path):
        fileString = ""
        if os.path.exists(path):
            with open(path,'r') as fileToRead:
                while True:
                    line = fileToRead.readline()
                    fileString = fileString + line
                    if not line:
                        break
        return fileString

    def saveResult(self,oldPath,newPath):
        shutil.copyfile(oldPath,newPath)
        return

    def deleteTempResaultFile(self,path):
        if os.path.exists(path):
            os.remove(path)
        else:
            return

    def tagNameMapping(self,name):
        if name == "Buses":
            return "bus"
        elif name == "Generators":
            return "gen"
        elif name == "Branches":
            return "branch"
        elif name == "GeneratorCosts":
            return "gencost"

    def convertDataToCase(self):
        ppc = {"version": '2'}

        ppc['baseMVA'] = 100.0
 
        for tag in DataBase.Instance.components:
            tempCollection = []
            for component in DataBase.Instance.components[tag]:
                attr = []
                for att in component.__dict__:
                        if att != "name" and att != "gid":
                            param = str(getattr(component,att))
                            if param.count("[") > 0:
                                for value in getattr(component,att):
                                    attr.append(value)
                            else :
                                attr.append(getattr(component,att))
                tempCollection.append(attr)
            ppc[self.tagNameMapping(tag)] = array(tempCollection)

        return ppc
    
pass

Instance = ExtensionMethod()