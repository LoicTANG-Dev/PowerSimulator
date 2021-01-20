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
        self.win.protocol("WM_DELETE_WINDOW", Controller.Instance.onComponentModifyingExit)
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
        if info.head == "GetComponentModifiedValue":
            Controller.Instance.onModifiedComponentValueReceived(info.param["gid"],self.getComponentValues())
        elif info.head == "ComponentModifiedDone" or info.head =="CloseComponentModifyingWin":
            self.win.destroy()
            Controller.Instance.onDestroyComponentModifyingWin()
    
pass