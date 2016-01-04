import pandas as pd
import os
import time
from datetime import datetime
import requests

#Mean recommendation: 1.0 (strong buy) .... 5.0 (strong sell) (analyst opinion)
#growth rate (this year)  (analyst estimate)


def main(features=['Total Debt/Equity (mrq)','Return on Equity (ttm)', 'Return on Assets (ttm)',
                   'Mean Recommendation (this week)', 'This Year', 'Market Cap (intraday)', 'Trailing P/E (ttm, intraday)',
                   'PEG Ratio(5 yr expected)', 'Price/Sales (ttm)', 'Price/Book (mrq)', 'Enterprise Value/Revenue (ttm)', 'Enterprise Value/EBITDA (ttm)', 'price' ]):
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
        df = pd.DataFrame(columns = ['Date', 'Name', 'Debt/Equity', 'Return On Equity', 'Return On Assets', 'Mean Recommendation', 'Growth Rate',
                                     'Market Cap', 'P/E Ratio', 'PEG Ratio', 'Price/Sales', 'Price/Book', 'EV/Revenue', 'EV/EBITDA', 'Price'])    
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
            value6 = data.split(features[5])[1].split('yfs_j10_' + stockName.lower() + '">')[1].split('</span>')[0]
            value7 = data.split(features[6] + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            value8 = 'z'#data.split(features[7])[1].split('class="yfnc_tabledata1">')[1].split('</td>')[0]
            value9 = data.split(features[8] + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            value10 = data.split(features[9] +  ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            value11 = 'z'#data.split(features[10] + 'class="yfnc_tabledata1">')[1].split('</td>')[0]
            value12 = 'z'#data.split(features[11] + 'class="yfnc_tabledata1">')[1].split('</td>')[0]
            value13 = data.split('yfs_l84_' + stockName.lower() + '">')[1].split('</span>')[0]
                                                                                             
            try:
                value5 = value5.split('#cc0000">')[1].split("</font>")[0]
            except:
                pass
            df = df.append({'Date':dateStamp, 'Name':stockName, 'Debt/Equity':str(value1), 'Return on Equity':str(value2), 'Return on Assets':str(value3), 'Mean Recommendation':str(value4),
                            'Growth Rate':str(value5), 'Market Cap':str(value6), 'P/E Ratio':str(value7), 'PEG Ratio':str(value8), 'Price/Sales':str(value9), 'Price/Book':str(value10),
                            'EV/Revenue':str(value11), 'EV/EBITDA':str(value12), 'Price':str(value13)}, ignore_index = True)
        except Exception as e:
            df = df.append({'Date':parsingError, 'Name':parsingError, 'Debt/Equity':parsingError, 'Return on Equity':parsingError, 'Return on  Assets':parsingError, 'Mean Recommendation':parsingError, 'Growth Rate':parsingError, 'Market Cap':parsingError, 'P/E Ratio':parsingError, 'PEG Ratio':parsingError, 'Price/Sales':parsingError, 'Price/Book':parsingError, 'EV/Revenue':parsingError, 'EV/EBITDA':parsingError, 'Price':parsingError}, ignore_index = True)
            print ('Unable to parse: ' + stockName)
            parseSuccessful = False
        if(parseSuccessful==True):
            print ("Showing fundamental data for: " + stockName + "\n", str(value1), str(value2), str(value3), str(value4), str(value5), str(value6), str(value7), str(value8), str(value9), str(value10), str(value11), str(value12), str(value13))
        
        

main()




##/*
##import pandas as pd
##import os
##import time
##from datetime import datetime
##import requests
##
##
##def main(feature='Total Debt/Equity (mrq)'):
##    
##    path = "C:/Users/sdd/"
##    stockName = input('Enter stock: ')
##    
##    url = 'https://ca.finance.yahoo.com/q/ks?s=' + stockName
##    df = pd.DataFrame(columns = ['Date', 'Name', 'Debt/Equity'])
##    
##    r = requests.get(url)
##    data = r.text
##    dateStamp = data.split('<span id="yfs_market_time">')[1].split('-')[0]
##    
##    value = data.split(feature + ':</td><td class="yfnc_tabledata1">')
##    value1 = value[1].split('</td>')
##    value2 = value1[0]
##    #print(stockName + "--" + feature + "............ " + value2 + " .............. " + dateStamp)
##
##    df = df.append({'Date':dateStamp, 'Name':stockName, 'Debt/Equity':value2}, ignore_index = True)
##
##    save = feature.replace('/','').replace('(','').replace(')','').replace(' ', '') +('.csv')
##    path = path + save
##    print(path)
##    df.to_csv(path)
##    
##    
##
##main()
##*/
