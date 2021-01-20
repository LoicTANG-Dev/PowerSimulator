from DataModule import Bus,Generator,Branch,GeneratorCost,DCLine
from DataModule import DataBase
from Common import Message

class ComponentFactory():
    
    def __init__(self):
        return 

    def parseParam(self,param):
        if param == "":
            return 0
        elif param.count("[") > 0:
            param = param.replace("[","")
            param = param.replace("]","")
            values = param.split(',')
            temp = []
            for value in values:
                temp.append(self.parseParam(value))
            return temp
        else:
            if param.count(".") > 0:
                return float(param)
            else:
                return int(param)
    
    def setComponentParam(self,com,arg):
        for argName in arg:
            if argName == "gid":
                setattr(com,argName,arg[argName])
            elif argName == "centerX" or argName == "centerY":
                continue
            else:
                setattr(com,argName,self.parseParam(arg[argName]))
    
    def generateMessage(self,fromXML,component,gid="",centerX=0,centerY=0):
        message = Message.Message("ComponentCreateDone")
        message.param["componentGid"] = gid
        message.param["component"] = component
        message.param["centerX"] = centerX
        message.param["centerY"] = centerY
        message.param["fromXML"] = fromXML
        return message

    def createComponent(self,fromXML,arg):
        global componentEle
        if arg[0] == "Bus":
            componentEle = Bus.Bus()
            self.setComponentParam(componentEle,arg[1])
            DataBase.Instance.components['Buses'].append(componentEle)
        elif arg[0] == "Generator":
            componentEle = Generator.Generator()
            self.setComponentParam(componentEle,arg[1])
            DataBase.Instance.components['Generators'].append(componentEle)
        elif arg[0] == "Branch":
            componentEle = Branch.Branch()
            self.setComponentParam(componentEle,arg[1])
            DataBase.Instance.components['Branches'].append(componentEle)
        elif arg[0] == "DCLine":
            componentEle = DCLine.DCLine()
            self.setComponentParam(componentEle,arg[1])
            DataBase.Instance.components['Dclines'].append(componentEle)
        elif arg[0] == "GeneratorCost":
            componentEle = GeneratorCost.GeneratorCost()
            self.setComponentParam(componentEle,arg[1])
            DataBase.Instance.components['GeneratorCosts'].clear()
            DataBase.Instance.components['GeneratorCosts'].append(componentEle)
        if fromXML == True:
            if arg[0] != "GeneratorCost":
                return self.generateMessage(fromXML,arg[0],arg[1]["gid"],int(arg[1]["centerX"]),int(arg[1]["centerY"]))
            else:
                return self.generateMessage(fromXML,arg[0])
        else:
            if arg[0] != "GeneratorCost":
                return self.generateMessage(fromXML,arg[0],arg[1]["gid"])
            else:
                return self.generateMessage(fromXML,arg[0])
            

pass

Instance = ComponentFactory()