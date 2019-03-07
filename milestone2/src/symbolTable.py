class SymbolTable:
    def __init__(self):
        self.table = {}
        self.parent = None

    def lookUp(self, name):
        return (name in self.table)

    def insert(self, name, value):
        if (not self.lookUp(name)):
            (self.table)[name] = value
            return 1
        else:
            return 0
 
    def getDetail(self, name):
        if(self.lookUp(name)):
            return self.table[name]
        else:
            return None

    def setParent(self, parent):
        self.parent = parent



