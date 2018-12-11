
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np



class TrainingData:
    def __init__(self, dataframe, percentage = 0.5):
        self.dataframe = dataframe
        self.percentage = percentage
    def SplitTrain(self):
        try:
            try: 
                rows = len(self.dataframe)
                train = round(rows*self.percentage)
            except:
                return ("Message: Attribute error, please give correct parameters")
            data = self.dataframe
            
            #drop = True, will keep its index without replacing it with a new index
            df = data.sample(frac=1, random_state=1).reset_index(drop=True)
            try: 
                trainingdata = df[0:train]
                testdata = df[train:rows]
                return (trainingdata, testdata)
            except:
                return ("Message: Index Error, please check inputs")
        except:
            return("Message: Can not split dataset")

