import pandas as pd

myDictionary = {
    'Name' : 'Deborah',
    'Number' : 42,
    'Age' : 'unknown'
    }

mySeries = pd.Series(myDictionary)
print(mySeries)
