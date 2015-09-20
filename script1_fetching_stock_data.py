import pandas as pd
import os
import time
from datetime import datetime
import requests


def main(features=['Total Debt/Equity (mrq)','Return on Equity (ttm)', 'Return on Assets (ttm)', 'Mean Recommendation (this week)', 'This Year']):
    df_stock_info = pd.DataFrame.from_csv('constituents.csv', index_col = False)
    alist = df_stock_info["Symbol"].tolist()
    parsingError = 'N/A'
    for x in range(0,280):
        #path = "C:/Users/sdd/"
        #input not working? #stockName = input("Enter stock: ") 

        
        #print(alist)
        parseSuccessful = True
        stockName = str(alist[x])
        urlFundamentals = 'https://ca.finance.yahoo.com/q/ks?s=' + stockName
        urlOpinion = 'https://ca.finance.yahoo.com/q/ao?s=' + stockName
        urlGrowthEstimate = 'https://ca.finance.yahoo.com/q/ae?s=' + stockName	
        df = pd.DataFrame(columns = ['Date', 'Name', 'Debt/Equity', 'Return On Equity', 'Return On Assets', 'Mean Recommendation', 'Growth Rate'])    
        r = requests.get(urlFundamentals)
        r2 = requests.get(urlOpinion)
        r3 = requests.get(urlGrowthEstimate)
        data = r.text
        data2 = r2.text
        data3 = r3.text
        dateStamp = data.split('<span id="yfs_market_time">')[1].split('-')[0]   
        values = []
        try:
            value1 = data.split(features[0] + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            value2 = data.split(features[1] + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0].replace('%','')
            value3 = data.split(features[2] + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0].replace('%','')
            value4 = data2.split(features[3] + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            value5 = data3.split(features[4] + '</td><td class="yfnc_tabledata1">')[1].split('</td>')[0].replace('%','')
            try:
                value5 = value5.split('#cc0000">')[1].split("</font>")[0]
            except:
                pass
            df = df.append({'Date':dateStamp, 'Name':stockName, 'Debt/Equity':str(value1), 'Return on Equity':str(value2), 'Return on  Assets':str(value3), 'Mean Recommendation':str(value4), 'Growth Rate':str(value5)}, ignore_index = True)
        except Exception as e:
            df = df.append({'Date':parsingError, 'Name':parsingError, 'Debt/Equity':parsingError, 'Return on Equity':parsingError, 'Return on  Assets':parsingError, 'Mean Recommendation':parsingError, 'Growth Rate':parsingError}, ignore_index = True)
            print 'Unable to parse: ' + stockName
            parseSuccessful = False
        if(parseSuccessful==True):
            print "Showing fundamental data for: " + stockName + "\n", str(value1), str(value2), str(value3), str(value4), str(value5)
        
        

main()
