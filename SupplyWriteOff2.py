from datetime import datetime
import pandas as pd
import traceback

def eat(pandasSeries, v):
    for i in range(len(pandasSeries)):
        if pandasSeries[i] - v >= 0:
            pandasSeries[i] -=  v
            v = 0

        else:
            v -= pandasSeries[i]
            pandasSeries[i] = 0

    return v




def calculateWriteOffs(dictMateriais, df, material, batch):
                try:
                    meses =list(df[material]['Meses'])
                    forecast = list(df[material]['Forecast'])
                    forecastReplica = None
                    
                    batchExpirationDict = {}

                    for batch in list(dictMateriais[material]['Batch'].keys()):
                        stockAmount = dictMateriais[material]['Batch'][batch].get('Stock Amount')
                        lsdString = dictMateriais[material]['Batch'][batch].get('Limit sales date')
                        limitSalesDate = datetime.strptime(lsdString, "%Y-%m-%d")
                        batchExpirationDict[batch] = limitSalesDate

                    orderedBatchList = sorted(batchExpirationDict.items(), key=lambda item: item[1])
                    limitMonth = None  
                    for batch in orderedBatchList:
                        print(limitSalesDate)    
                        previousLimitMonth = limitMonth
                        for m in meses:
                            try:
                            #print(m,"MES")
                                dateObj = datetime.strptime(m.lower(), "%b %Y")
                                if dateObj < limitSalesDate:
                                    limitMonth = dateObj.strftime("%b %Y").upper()
                            except:
                                ...                        
                        if limitMonth != None:
                            idx = meses.index(limitMonth)
                            if forecastReplica == None or previousLimitMonth != limitMonth:
                                _meses = meses[:idx + 1]
                                _forecast = forecast[:idx + 1]
                                forecastReplica = pd.Series(data=_forecast, index=_meses)
                            print(forecastReplica)
                            print(stockAmount)
                            wo = eat(forecastReplica, stockAmount)
                            print(forecastReplica)
                            for i in range(len(forecastReplica)):
                               meses[i] = forecastReplica[i] 
                            dictMateriais[material]['Batch'][batch[0]]["Write off"] = wo
                            print(batch,wo)

                except:
                    traceback.print_exc()

                    print("AQUI",df[key], "aqui")
                    ...