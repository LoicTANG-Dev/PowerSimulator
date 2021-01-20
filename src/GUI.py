import tkinter
import sys,gc
from tkinter import WORD,END,scrolledtext
from tkinter import filedialog as filedialog
from tkinter import messagebox
from ControlModule import Controller as Controller
from Common import Observer,Message
from GUIModule import ResultWindow,ComponentCreatingWin,WindowFactory
from GUIDataModule import GUIData,GUIComponentFactory

class GUI(Observer.Observer):

    win = None
    canvas = None
    filePathEntery = None
    entryVariable = None
    selectMapFileButton = None
    readXMLButton = None
    writeXMLButton = None
    menubar = None
    componentCreatingWin = None
    componentModifyingWin = None
    rightButtonMenu = None

    def __init__(self):

        self.componentCreatingWin = None
        self.componentModifyingWin = None

        self.win = tkinter.Tk()
        self.win.title('Power Simulator')
        self.win.protocol("WM_DELETE_WINDOW", Controller.Instance.onExit)

        #main window positioning
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()
        winWidth = 1000
        winHeight = 600
        winX = (screenWidth-winWidth)/2
        winY = (screenHeight-winHeight)/2
        self.win.geometry('%dx%d+%d+%d'%(winWidth,winHeight,winX,winY))

        #canvas component
        self.canvas = tkinter.Canvas(self.win,width=1000,height=600)

        #Manu Bar
        self.menubar = tkinter.Menu(self.win)
        self.setMenu()
        self.win['menu'] = self.menubar

        #Right Button Menu
        self.rightButtonMenu = tkinter.Menu(self.win,tearoff=0)
        self.rightButtonMenu.add_command(label="Delete",command=Controller.Instance.deleteCurrentSelectedComponent)
        self.rightButtonMenu.add_command(label="Modify",command=Controller.Instance.modifiyCurrentSelectedComponent)
        
        #events
        self.win.bind("<Button-1>",Controller.Instance.mouseLeftButtonClicked)
        self.win.bind("<Button-3>",Controller.Instance.mouseRightButtonCLicked)

    def selectFilePath(self):
        fileDiag = filedialog.askopenfilename()
        GUIData.Instance.filePath = fileDiag
    
    def openTempResultWindow(self):
        resultWin = ResultWindow.ResultWindow()
        resultWin.show()
        
    def showComponentCreatingWin(self,component):
        self.componentCreatingWin = WindowFactory.Instance.createComponentCreatingWin(component)
        self.componentCreatingWin.show()
    
    def showComponentModifyingWin(self,tag,componentInstance):
        self.componentModifyingWin = WindowFactory.Instance.createComponentModifyingWin(tag,componentInstance)
        self.componentModifyingWin.show()
    
    def drowBus(self,centerX,centerY):
        self.canvas.create_line((centerX,centerY-30),(centerX,centerY+30),width=3)
        self.canvas.pack()
    
    def drowGenerator(self,centerX,centerY):
        self.canvas.create_oval(centerX-15,centerY-15,centerX+15,centerY+15)
        self.canvas.create_line((centerX-15,centerY),(centerX+15,centerY),width=1)
        self.canvas.pack()

    def drowBranch(self,centerX,centerY):
        self.canvas.create_rectangle((centerX-10,centerY-10),(centerX+10,centerY+10),fill="red")
        self.canvas.create_line((centerX-15,centerY),(centerX-10,centerY),width=1)
        self.canvas.create_line((centerX+10,centerY),(centerX+15,centerY),width=1)
        self.canvas.pack()

    def drowDCLine(self,centerX,centerY):
        self.canvas.create_rectangle((centerX-10,centerY-10),(centerX+10,centerY+10),fill="black")
        self.canvas.create_line((centerX-15,centerY),(centerX-10,centerY),width=1)
        self.canvas.create_line((centerX+10,centerY),(centerX+15,centerY),width=1)
        self.canvas.pack()
    
    def drowLine(self,startX,startY,endX,endY):
        self.canvas.create_line((startX,startY),(endX,endY),width=1)
        self.canvas.pack()

    def paintComponent(self,ele):
        if ele.name == "Bus":
            self.drowBus(ele.centerPosition['x'],ele.centerPosition['y'])
        elif ele.name == "Generator":
            self.drowGenerator(ele.centerPosition['x'],ele.centerPosition['y'])
            self.drowLine(ele.centerPosition['x'],ele.centerPosition['y']-15,ele.centerPosition['x'],ele.centerPosition['y']-20)
            self.drowLine(ele.centerPosition['x'],ele.centerPosition['y']-20,ele.genbusPosition["x"],ele.genbusPosition["y"])
        elif ele.name == "Branch":
            self.drowBranch(ele.centerPosition['x'],ele.centerPosition['y'])
            self.drowLine(ele.fbusPosition["x"],ele.fbusPosition["y"],ele.centerPosition["x"]-15,ele.centerPosition["y"])
            self.drowLine(ele.centerPosition["x"]+15,ele.centerPosition["y"],ele.tbusPosition["x"],ele.tbusPosition["y"])
        elif ele.name == "DCLine":
            self.drowDCLine(ele.centerPosition['x'],ele.centerPosition['y'])
            self.drowLine(ele.fbusPosition["x"],ele.fbusPosition["y"],ele.centerPosition["x"]-15,ele.centerPosition["y"])
            self.drowLine(ele.centerPosition["x"]+15,ele.centerPosition["y"],ele.tbusPosition["x"],ele.tbusPosition["y"])

    def refreshCanvas(self):
        self.canvas.delete("all")
        for component in GUIData.Instance.components:
            for ele in GUIData.Instance.components[component]:
                self.paintComponent(ele)

    def setMenu(self):
        #region File Menu
        fileSubmenu = tkinter.Menu(self.menubar,tearoff=0)
        fileSubmenu.add_command(label="load map from xml",command=Controller.Instance.readXMLButtonClicked)
        fileSubmenu.add_command(label="save as xml",command=Controller.Instance.writeXMLButtonClicked)
        self.menubar.add_cascade(label="File",menu=fileSubmenu)

        #region Analyze Menu
        analyzeSubmenu = tkinter.Menu(self.menubar, tearoff=0)
        analyzeSubmenu.add_command(label="dcpf",command=lambda:Controller.Instance.algoClicked("dcpf"))
        self.menubar.add_cascade(label="Analyze",menu=analyzeSubmenu)

        #region Create Component
        componentCreatingSubmenu = tkinter.Menu(self.menubar, tearoff=0)
        componentCreatingSubmenu.add_command(label="Bus",command=lambda:Controller.Instance.createComponentClicked("Bus"))
        componentCreatingSubmenu.add_command(label="Generator",command=lambda:Controller.Instance.createComponentClicked("Generator"))
        componentCreatingSubmenu.add_command(label="Branch",command=lambda:Controller.Instance.createComponentClicked("Branch"))
        componentCreatingSubmenu.add_command(label="DCLine",command=lambda:Controller.Instance.createComponentClicked("DCLine"))
        componentCreatingSubmenu.add_command(label="Set Generator Cost",command=lambda:Controller.Instance.createComponentClicked("GeneratorCost"))
        self.menubar.add_cascade(label="Components",menu=componentCreatingSubmenu)
    
    def popRightButtonMenu(self,x,y):
        self.rightButtonMenu.post(x,y)

    def listen(self,info):
        print(info.head)
        if info.head == "OpenXmlReader":
            self.selectFilePath()
            Controller.Instance.readXmlFile()
        elif info.head =="OpenXmlWriter":
            self.selectFilePath()
            Controller.Instance.writeXmlFile()
            return
        elif info.head == "ReadDone" or info.head == "CreateDone":
            GUIData.Instance.clearFilePath()
            infoString = ""
            if info.head == "ReadDone":
                infoString = "Load map from XML file: Done !"
            elif info.head == "CreateDone":
                infoString = "Save XML file: Done !"
            if infoString != "":
                tkinter.messagebox.showinfo("Infomation",infoString)
        elif info.head == "ResultSaveDone":
            tkinter.messagebox.showinfo("Infomation","Save result: Done !")
            GUIData.Instance.clearFilePath()
        elif info.head =="AnalysefDone":
            self.openTempResultWindow()
        elif info.head =="DeleteTempFileDone":
            sys.exit(0)
        elif info.head =="ShowComponentCreatingWin":
            if info.param["type"] == "Bus":
                self.showComponentCreatingWin("Bus")
            elif info.param["type"] == "Branch":
                self.showComponentCreatingWin("Branch")
            elif info.param["type"] == "Generator":
                self.showComponentCreatingWin("Generator")
            elif info.param["type"] == "GeneratorCost":
                self.showComponentCreatingWin("GeneratorCost")
            elif info.param["type"] == "DCLine":
                self.showComponentCreatingWin("DCLine")
        elif info.head == "ShowComponentMotifyingWin":
            if info.param["type"] == "Bus":
                self.showComponentModifyingWin("Bus",info.param["component"])
            elif info.param["type"] == "Branch":
                self.showComponentModifyingWin("Branch",info.param["component"])
            elif info.param["type"] == "Generator":
                self.showComponentModifyingWin("Generator",info.param["component"])
            elif info.param["type"] == "GeneratorCost":
                self.showComponentModifyingWin("GeneratorCost",info.param["component"])
            elif info.param["type"] == "DCLine":
                self.showComponentModifyingWin("DCLine",info.param["component"])
        elif info.head == "RemoveObserverComponentCreatingWin":
            del self.componentCreatingWin
            Controller.Instance.removeObserver(self.componentCreatingWin)
        elif info.head == "RemoveObserverComponentModifyingWin":
            del self.componentModifyingWin
            Controller.Instance.removeObserver(self.componentModifyingWin)
        elif info.head == "ComponentCreateDone":
            if info.param["fromXML"] == False:
                if info.param["component"] != "GeneratorCost":
                    GUIComponentFactory.Instance.createComponent(info.param["component"],info.param["componentGid"],info.param["fromXML"])
                    GUIData.Instance.clearClickPosition()
                    self.refreshCanvas()
            else:
                if info.param["component"] != "GeneratorCost":
                    GUIComponentFactory.Instance.createComponent(info.param["component"],info.param["componentGid"],info.param["fromXML"],info.param["centerX"],info.param["centerY"])
                    self.refreshCanvas()
        elif info.head == "FreshGUIComponent":
            GUIComponentFactory.Instance.refreshGUIComponent(info.param["referenceInstanceGid"])
            self.refreshCanvas()
        elif info.head == "PopRightButtonMenu":
            print(info.param["eventX"])
            print(info.param["eventY"])
            self.popRightButtonMenu(info.param["eventX"],info.param["eventY"])
        elif info.head == "DataBaseUpdated":
            self.refreshCanvas()

    pass

gui = GUI()
Controller.Instance.registerObserver(gui)
gui.win.mainloop()

