from GUIModule import SubWindow
import tkinter
from GUIModule import WindowFactory
from ControlModule import Controller

class ComponentCreatingWin(SubWindow.SubWindow):

    confirmButton = None
    cancelButton = None
    attrPair = []

    def __init__(self):
        SubWindow.SubWindow.__init__(self)
        self.confirmButton = None
        self.cancelButton = None
        self.attrPair = []
        self.win.protocol("WM_DELETE_WINDOW", Controller.Instance.onComponentCreatingExit)
        Controller.Instance.registerObserver(self)

    def getComponentValues(self):
        ComponentValues = {}
        for attr in self.attrPair:
            label = attr[0]
            entry = attr[1]
            ComponentValues[label['text']] = entry.get()
        return ComponentValues
    
    def listen(self,info):
        print(info.head)
        if info.head == "GetComponentValueBus":
            Controller.Instance.onComponentValueReceived("Bus",self.getComponentValues())
        elif info.head == "GetComponentValueBranch":
            Controller.Instance.onComponentValueReceived("Branch",self.getComponentValues())
        elif info.head == "GetComponentValueGenerator":
            Controller.Instance.onComponentValueReceived("Generator",self.getComponentValues())
        elif info.head == "GetComponentValueGeneratorCost":
            Controller.Instance.onComponentValueReceived("GeneratorCost",self.getComponentValues())
        elif info.head == "GetComponentValueDCLine":
            Controller.Instance.onComponentValueReceived("DCLine",self.getComponentValues())
        elif info.head == "ComponentCreateDone" or info.head =="CloseComponentCreatingWin":
            self.win.destroy()
            Controller.Instance.onDestroyComponentCreatingWin()
            
pass