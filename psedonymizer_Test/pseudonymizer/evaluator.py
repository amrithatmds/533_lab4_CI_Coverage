from pseudonymizer import anonymizer
import pandas as pd
import numpy as np

class Ldiversity(anonymizer.AttrIdentifier):
    def __init__(self, type, func):
        try: # only for error handling demonstration
            func = func.lower() 
        except:
            print ("Object cannot be created, please pass string for func parameter")
        else:
            anonymizer.AttrIdentifier.__init__(self, type)
            self.func = func
        
    def ldivMaxProb(self, df, qcols, scolumns):
        
        df = df
        qcols = qcols
        scols = scolumns
        
        try:
            df = df[qcols + scols]
            df = df.sort_values(qcols)
        except:
            print ("The qcols and scolumns both need to be lists")
            return -1
                
        maxProb = 0
        for i in df.groupby(qcols):
            lst = [x for x in i[1][scols].values]
            kgrp = []
            for item in lst:
                kgrp.append(int(item))
            uniq = len(set(kgrp))
            maxProb = max(maxProb, 1/uniq)
                
        return maxProb