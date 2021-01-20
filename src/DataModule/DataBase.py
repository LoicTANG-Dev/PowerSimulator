class DataBase:

    components = {}

    def __init__(self):
        self.components['Buses'] = []
        self.components['Generators'] = []
        self.components['Branches'] = []
        self.components['Dclines'] = []
        self.components['GeneratorCosts'] = []
    
    def deleteComponent(self,gid):
        flag = False
        componentToDelete = self.findComponentByGid(gid)
        if componentToDelete != None:
            for component in self.components:
                for ele in self.components[component]:
                    if ele == componentToDelete:
                        flag = True
                        self.components[component].remove(ele)
                        break
                if flag == True:
                    break

    def showComponents(self):
        for component in self.components:
            for ele in self.components[component]:
                ele.showParam()

    def findComponentByGid(self,gid):
        find = None
        for component in self.components:
            for ele in self.components[component]:
                if ele.gid == gid:
                    find = ele
                    break
            if find != None:
                break
        return find
    
    def findBusById(self,id):
        find = None
        for ele in self.components["Buses"]:
            if ele.busId == id:
                find = ele
                break
        return find

pass

Instance = DataBase()