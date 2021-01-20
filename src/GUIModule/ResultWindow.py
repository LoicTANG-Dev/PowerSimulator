import tkinter
from GUIModule import SubWindow
from GUIDataModule import GUIData
from tkinter import WORD,END,scrolledtext
from tkinter import filedialog as filedialog
from ControlModule import Controller as Controller

class ResultWindow(SubWindow.SubWindow):
    
    def __init__(self):

        SubWindow.SubWindow.__init__(self)
        self.win.title("Analyse Result")
        self.win.geometry('%dx%d+%d+%d'%(745,500,30,30))
        self.win.resizable(width=False,height=False)
        resultString = Controller.Instance.getTempResult()
        self.text = scrolledtext.ScrolledText(self.win,wrap=WORD,width=103,height=40)
        self.text.insert(END,resultString)
        self.text.grid(column=0,row=0,rowspan=2)
        menuBar = tkinter.Menu(self.win)
        menuBar.add_command(label="save",command=Controller.Instance.saveResultClicked)
        self.win["menu"] = menuBar
        Controller.Instance.registerObserver(self)

    def listen(self,info):
        if info.head == "SaveResult":
            fileDiag = filedialog.askopenfilename()
            GUIData.Instance.filePath = fileDiag
            Controller.Instance.saveResult()

pass