import xml.etree.ElementTree as Et
#import os
from DataModule import DataBase

class XmlWriter:

    #fileFolder=''

    def __init__(self):
        return
        
    def __indent(self,elem,level=0):

        i = "\n" + level*"\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.__indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
        

    def createXMLFile(self,path,guiComponents):

        root = Et.Element("Components")
        tree = Et.ElementTree(root)

        for componentNames in DataBase.Instance.components:
            ele = Et.Element(componentNames)
            root.append(ele)
        
        componentCollection = root.getchildren()

        for componentNode in componentCollection:
            for component in DataBase.Instance.components[componentNode.tag]:
                childELe = Et.Element(component.name)
                for attr in component.__dict__:
                    if attr != "name":
                        childELe.set(attr,str(getattr(component,attr)))
                find = False
                for guiComponent in guiComponents:
                    for guiComponentEle in guiComponents[guiComponent]:
                        if component.name != "GeneratorCost" and guiComponentEle.referenceInstanceGid == component.gid:
                            childELe.set("centerX",str(guiComponentEle.centerPosition["x"]))
                            childELe.set("centerY",str(guiComponentEle.centerPosition["y"]))
                            find = True
                            break
                    if find == True:
                        break
                componentNode.append(childELe)
        
        self.__indent(root)

        tree.write(path,encoding='utf-8',xml_declaration=True)

