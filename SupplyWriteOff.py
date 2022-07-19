from datetime import datetime
import pandas as pd


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