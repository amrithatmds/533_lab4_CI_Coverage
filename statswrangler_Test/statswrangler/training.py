
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
                print ("Message: Attribute error, please give correct parameters")
                return None
            data = self.dataframe
            
            #drop = True, will keep its index without replacing it with a new index
            df = data.sample(frac=1, random_state=1).reset_index(drop=True)
            trainingdata = df[0:train]
            testdata = df[train:rows]
            return (trainingdata, testdata)
 
        except:
            print("Message: Can not split dataset")
            return None

