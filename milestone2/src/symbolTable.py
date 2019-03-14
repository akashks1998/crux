class SymbolTable:
    def __init__(self,parent=None):
        self.table = {}
        self.parent = parent

    def lookUp(self, name):
        return (name in self.table)
    
    def delete(self, name):
        (self.table).pop(name, None)

    def insert(self, name, value):
        if (not self.lookUp(name)):
            (self.table)[name] = value
            return True
        else:
            return False
    
    def update(self, name, value):
        (self.table)[name] = value
        return True

 
    def getDetail(self, name):
        if(self.lookUp(name)):
            return self.table[name]
        else:
            return None

    def setParent(self, parent):
        self.parent = parent

    



