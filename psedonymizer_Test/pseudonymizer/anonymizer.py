import pandas as pd

class AttrIdentifier:


    def __init__(self, type):
        self.type = type
        self.quasiId = ('postal_code', 'zip_code', 'DOB', 'dateofbirth', 'age', 'gender', 'city') 
        self.explicitId = ('name', 'sin', 'email', 'cell_number', 'phone_number')
        self.sensitiveId = ('disease', 'disability', 'health_condition', 'salary', 'income')
        
    def suggest(self, columnNames):
        colNames = columnNames
        qId = []
        sensId = []
        suggestion = {}
        quasiId = self.getQuasiId()
        sensitiveId = self.getSensitiveId()
    
        for name in colNames:
            try: # this is just for error-handling demonstration, the type can be handled in the class
                if name.lower() in [x.lower() for x in quasiId]: # from the tuple take each item and convert it to lowercase and compare with the string
                    qId.append(name)
            except:
                print ("Check column name data types, they have to be strings")
                return -1
            
        for name in colNames:
            if str(name).lower() in [x.lower() for x in sensitiveId]:
                sensId.append(name)
                
        suggestion['qId'] = qId
        suggestion['sensId'] = sensId
        return suggestion
    
    def setQuasiId(self, quasiIds):
        self.quasiId = quasiIds
        
    def getQuasiId(self):
        return self.quasiId
    
    def setSensitiveId(self, sensId):
        self.sensitiveId = sensId
        
    def getSensitiveId(self):
        return self.sensitiveId
    
    def setType(self, type):
        self.type = type
        
    def getType(self):
        return self.type

class Anonymizer(AttrIdentifier):
    def __init__(self, type, func):
        AttrIdentifier.__init__(self, type)
        self.func = func
    
    def kcounter(self, df, qcolumns):
        df = df
        qcols = qcolumns
        try:
            df = df[qcols]
        except:
            print ("Please check the dataframe, the columns you specified are not in the dataframe")
            return -1
        try:
            df = df.sort_values(qcols)
            k = df.groupby(qcols).size().min()
        except:
            print ("Please pass a valid set of column values to kcounter function")
            return -1
        return k