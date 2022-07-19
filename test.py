a = ['-',2,3,4,5,6]
b = [2,3,4,5,6,7]
d = {'col1': a, 'col2': b}

c = [2, '-',6]
d2 = {'a': 2, 'b': '-', 'c': 6}
d3 = {'a': 2, 'b': 4, 'c': 6}
import pandas as pd
import numpy as np

series = pd.Series(data=d2)
series = pd.to_numeric(series, errors='coerce')
series2 = pd.Series(data=d3)
df = pd.DataFrame(data=d)

df['col1'] = pd.to_numeric(df['col1'], errors='coerce')

# arr1 = df[['col1']].to_numpy()

# arr2 = df[['col2']].to_numpy()

# print(arr1)
# print(arr2)

# print(type(arr1))

# arr3 = arr1 + arr2

# print(arr3)

# df[['col3']] = arr3

print(df)

print(list(df.col1))


# print(series.to_numpy() + series2.to_numpy())



from datetime import datetime
a = datetime.strptime("1900-01-02", "%Y-%m-%d")

b = datetime.strptime("1900-10-03", "%Y-%m-%d")


# print(a < b)

c = datetime.strptime('APR 2022'.lower(), '%b %Y' )

# print(c)
# print(a < c)


# df[code]['Forecast']

def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1




def eat(pandasSeries, v):
    for i in range(len(pandasSeries)):
        if pandasSeries[i] - v >= 0:
            pandasSeries[i] -=  v
            v = max(v - pandasSeries[i], 0)

        else:
            v -= pandasSeries[i]
            pandasSeries[i] = 0

    return v




def calculateWriteOffs(dictMateriais, df):
    for material in list(dictMateriais.keys()):
        print(material)

        for key in list(df.keys()):
            meses =list(df[key]['Meses'])
            forecast = list(df[key]['Forecast'])
            forecastReplica = None
            
            

            if key == material:
            
                batchExpirationDict = {}

                for batch in list(dictMateriais[material]['Batch'].keys()):
                    stockAmount = dictMateriais[material]['Batch'][batch].get('Stock Amount')
                    lsdString = dictMateriais[material]['Batch'][batch].get('Limit sales date')
                    limitSalesDate = datetime.strptime(lsdString, "%Y-%m-%d")
                    batchExpirationDict[batch] = limitSalesDate

                orderedBatchList = sorted(batchExpirationDict.items(), key=lambda item: item[1])  
                for batch in orderedBatchList:    
                    limitMonth = meses[0]
                    for m in meses:
                        dateObj = datetime.strptime(m.lower(), "%b %Y")
                        if dateObj < limitSalesDate:
                            limitMonth = dateObj.strf("%b %Y").upper()

                    idx = meses.index(limitMonth)
                    _meses = meses[:idx + 1]
                    forecastReplica = pd.Series(data=forecast, index=_meses)
                    wo = eat(forecastReplica, stockAmount)
                    dictMateriais[material]['Batch'][batch]["Write off"] = wo




lsdString = ['2020-01-10', '2021-07-20', '2019-05-05']
lsdDatetime = []

for d in lsdString:
    lsdDatetime.append(datetime.strptime(d, "%Y-%m-%d"))

print(lsdDatetime)


a = {'x': 3, 'y':2}

print(sorted(a.items(), key=lambda item: item[1]))







mergeSort(lsdDatetime)

print(lsdDatetime)



# Isso é VERDADEIRO

# m = ['apr', 'may', 'jun']
# f = [4, 5, 6]

# s = pd.Series(data=f, index=m)


# print(s)
# print(s[m[2]])




