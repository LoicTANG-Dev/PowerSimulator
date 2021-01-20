import tkinter
import datetime
from GUIModule import ComponentCreatingWin,ComponentModifyingWin
from GUIDataModule import GUIData
from ControlModule import Controller
class WindowFactory:

    def __init__(self):
        return

    def createComponentCreatingWin(self,component):
        componentCreatingWin = ComponentCreatingWin.ComponentCreatingWin()
        componentCreatingWin.win.title(component)
        componentCreatingWin.attrPair = self.setComponentWindow(component,componentCreatingWin.win)
        return componentCreatingWin

    def createComponentModifyingWin(self,tag,componentInstance):
        componentModifyingWin = ComponentModifyingWin.ComponentCreatingWin()
        componentModifyingWin.win.title(componentInstance.gid)
        componentModifyingWin.attrPair = self.setComponentModifyingWin(tag,componentInstance,componentModifyingWin.win)
        return componentModifyingWin
    
    def setComponentWindow(self,component,win):
        win.geometry('%dx%d+%d+%d'%(300,600,800,100))
        attrPair = self.generateWinEleByAttr(win,component)
        return attrPair
    
    def setComponentModifyingWin(self,tag,componentInstance,win):
        win.geometry('%dx%d+%d+%d'%(300,600,800,100))
        attrPair = self.generateModifyingWinEleByAttr(win,tag,componentInstance)
        return attrPair

    def createStringVar(self,value):
        stringvar = tkinter.StringVar()
        stringvar.set(value)
        return stringvar

    def generateModifyingWinEleByAttr(self,win,tag,componentInstance):
        indexRow = 0
        labelentryPair = []
        for attr in GUIData.Instance.componentAttrs[tag]:
            stringVar = tkinter.StringVar()
            stringVar = self.createStringVar(getattr(componentInstance,attr))
            attrLabel = tkinter.Label(win,text=attr,width=10)
            attrEntry = tkinter.Entry(win,textvariable=stringVar)
            attrLabel.grid(row=indexRow,column=0)
            attrEntry.grid(row=indexRow,column=1)
            labelentryPair.append((attrLabel,attrEntry))
            indexRow = indexRow + 1
        br = tkinter.Label(win,text="")
        br.grid(row=indexRow,column=0)
        br2 = tkinter.Label(win,text="")
        br2.grid(row=indexRow+1,column=0)
        confirmButton = tkinter.Button(win,text="Ok",width=10,command=lambda: Controller.Instance.confirmModifyingComponentClicked(componentInstance.gid))
        confirmButton.grid(row=indexRow+1,column=1)
        return labelentryPair

    def generateWinEleByAttr(self,win,component):
        indexRow = 0
        labelentryPair = []
        for attr in GUIData.Instance.componentAttrs[component]:
            stringVar = tkinter.StringVar()
            if attr == "gid":
                stringVar = self.createStringVar(component.title()+datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M%S'))
            attrLabel = tkinter.Label(win,text=attr,width=10)
            attrEntry = tkinter.Entry(win,textvariable=stringVar)
            attrLabel.grid(row=indexRow,column=0)
            attrEntry.grid(row=indexRow,column=1)
            labelentryPair.append((attrLabel,attrEntry))
            indexRow = indexRow + 1
        br = tkinter.Label(win,text="")
        br.grid(row=indexRow,column=0)
        br2 = tkinter.Label(win,text="")
        br2.grid(row=indexRow+1,column=0)
        confirmButton = tkinter.Button(win,text="Ok",width=10,command=lambda: Controller.Instance.confirmCreatingComponentClicked(component))
        confirmButton.grid(row=indexRow+1,column=1)
        return labelentryPair

            
pass

Instance = WindowFactory()