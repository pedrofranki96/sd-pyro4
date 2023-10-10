class User(object):
    name = ""
    key = ""

    def __init__(self, name, key):
        self.name = name
        self.key = key

    def getName(self):
        return self.name    
    
    def getKey(self):
        return self.key
    
    def setName(self, name):    
        self.name = name
    
    def setKey(self, key):  
        self.key = key
