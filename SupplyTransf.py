from datetime import datetime
import pandas as pd
import traceback


def calculateTransfer(dictMateriais, df):
    for material in list(dictMateriais.keys()):
        #print(material)

        for key in list(df.keys()):
            #print(key)
            if key == material:
                try:
                    forecast = list(df[key]['Forecast'])
                    forecastReplica = pd.Series()
                    
                    batchExpirationDict = {}
                    batchStockAmountDict = {}
                    batchBSKDict = {}
                    batchPlantDict = {}


                    for batch in list(dictMateriais[material]['Batch'].keys()):
                        
                        lsdString = dictMateriais[material]['Batch'][batch].get('Limit sales date')
                        limitSalesDate = datetime.strptime(lsdString, "%Y-%m-%d")
                        batchExpirationDict[batch] = limitSalesDate
                        batchStockAmountDict[batch] = dictMateriais[material]['Batch'][batch].get('Stock Amount')
                        batchBSKDict[batch] = dictMateriais[material]['Batch'][batch].get('Batch status key')
                        batchPlantDict[batch] = dictMateriais[material]['Batch'][batch].get('Plant')
                    
                    orderedBatchList = sorted(batchExpirationDict.items(), key=lambda item: item[1])
                    totalAmount = 0
                    for batch in orderedBatchList:
                        print(batchBSKDict[batch[0]])
                        print(batchBSKDict[batch[0]] == 0)
                        print(batchPlantDict[batch[0]])
                        if batchBSKDict[batch[0]] == 0 and batchPlantDict[batch[0]] == "BR08":
                            totalAmount += batchStockAmountDict[batch[0]]
                            #print(totalAmount)
                    fc = forecast[0]
                    #print(fc)
                    try:
                        forcastPercentage = (totalAmount / fc) * 100  
                        if forcastPercentage < 150:
                            print(batch, "resultado", forcastPercentage)
                    
                    except:
                        ...

                except:
                    ...