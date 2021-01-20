import json

class GeneratorCost():

    name = "GeneratorCost"
    gid = 0
    model = 0
    startup = 0
    shutdown = 0
    ncost = 0
    cost = []

    def __init__(self):
        self.gid = 0
        self.model = 0
        self.startup = 0
        self.shutdown = 0
        self.ncost = 0
        self.cost = []

    def init(self, model, startup, shutdown, ncost, cost):
        self.model = model
        self.startup = startup
        self.shutdown = shutdown
        self.ncost = ncost
        self.cost = cost

    def showParam(self):
        param = json.dumps(self,default=lambda obj: obj.__dict__, sort_keys= True,indent=4)
        print("GeneratorCost: "+param)

pass
