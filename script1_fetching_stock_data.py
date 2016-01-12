import pandas as pd
import os
import time
from datetime import datetime
import requests

def main():
    while(True):
        print('A) Refresh stock data')
        print('B) View stocks by Sector')
        print('C) View current screener settings')
        print('D) Modify stock screener')
        print('E) View best performing stocks')
        print('X) Exit')
        k = input('>> ')
        if(k == 'A'):
            mainp()
        elif(k == 'B'):
            sortStocks()
        elif(k == 'C'):
            modifyScreener()
        elif(k == 'D'):
            rankStocks()
        elif(k == 'X'):
            print('Exiting')
            break
        else:
            print('Invalid entry')
        
            
    

def refreshStocks():
    print('in refreshStocks method')
    grabData()

def sortStocks():
    print('in sortStocks method')
    df2_stock_info = pd.DataFrame.from_csv('C:/Users/Babbu/Desktop/constituents2.csv', index_col = False)
    sectorList=['Industrials', 'Health Care', 'Information Technology', 'Financials', 'Consumer Discretionary',
                          'Utilities', 'Materials', 'Energy', 'Consumer Staples', 'Telecommunications Services']
    for s in sectorList:
        currentSector = (df2_stock_info[s].tolist())
        currentSector = [x for x in currentSector if x != '0']
        print(s)
        print(currentSector)

def currentScreenerSettings():
    print('in current screener settings')
    print('Stocks are filtered if they fail to meet the following criteria:')
    #need to do more research on what defines a good filter
    #
    #

def modifyScreener():
    print('in modify method')
    

def rankStocks():
    print('in rank method')

def rankPEG():
    print('rank PEG method:')
    


#Mean recommendation: 1.0 (strong buy) .... 5.0 (strong sell) (analyst opinion)
#growth rate (this year)  (analyst estimate)

def mainp(features=['Total Debt/Equity (mrq)','Return on Equity (ttm)', 'Return on Assets (ttm)',
                   'Mean Recommendation (this week)', 'This Year', 'Market Cap (intraday)', 'Trailing P/E (ttm, intraday)',
                   'PEG Ratio (5 yr expected)', 'Price/Sales (ttm)', 'Price/Book (mrq)', 'Enterprise Value/Revenue (ttm)', 'Enterprise Value/EBITDA (ttm)', 'price' ]):
    #print('in grab data method')
    df_stock_info = pd.DataFrame.from_csv('C:/Users/Babbu/Desktop/constituents.csv', index_col = False)
    df2_stock_info = pd.DataFrame.from_csv('C:/Users/Babbu/Desktop/constituents2.csv', index_col = False)
    #alist = df_stock_info["Symbol"].tolist()
    parsingError = 'N/A'
    sectorList=['Industrials', 'Health Care', 'Information Technology', 'Financials', 'Consumer Discretionary',
                          'Utilities', 'Materials', 'Energy', 'Consumer Staples', 'Telecommunications Services']
    #reload the csv file's stocks into a single list in case any stocks were changed 
    blist = []
    for s in sectorList:
        blist.extend(df2_stock_info[s].tolist())
    blist = [x for x in blist if x != '0']
    print(blist)
    for x in range(0,280):
        #path = "C:/Users/sdd/"
        #input not working? #stockName = input("Enter stock: ") 

        
        #print(alist)
        parseSuccessful = True
        stockName = str(blist[x])
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
            value8 = data.split(features[7])[1].split('class="yfnc_tabledata1">')[1].split('</td>')[0]
            value9 = data.split(features[8] + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            value10 = data.split(features[9] +  ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
            value11 = data.split(features[10])[1].split('tabledata1">')[1].split('</td>')[0]
            value12 = data.split(features[11])[1].split('tabledata1">')[1].split('</td>')[0]
            value13 = data.split('yfs_l84_' + stockName.lower() + '">')[1].split('</span>')[0]
                                                                                             
            try:
                value5 = value5.split('#cc0000">')[1].split("</font>")[0]
            except:
                pass
            df = df.append({'Date':dateStamp, 'Name':stockName, 'Debt/Equity':str(value1), 'Return on Equity ':str(value2), 'Return on Assets':str(value3), 'Mean Recommendation':str(value4),
                            'Growth Rate':str(value5), 'Market Cap':str(value6), 'P/E Ratio':str(value7), 'PEG Ratio':str(value8), 'Price/Sales':str(value9), 'Price/Book':str(value10),
                            'EV/Revenue':str(value11), 'EV/EBITDA':str(value12), 'Price':str(value13)}, ignore_index = True)
        except Exception as e:
            df = df.append({'Date':parsingError, 'Name':parsingError, 'Debt/Equity':parsingError, 'Return on Equity':parsingError, 'Return on  Assets':parsingError, 'Mean Recommendation':parsingError, 'Growth Rate':parsingError, 'Market Cap':parsingError, 'P/E Ratio':parsingError, 'PEG Ratio':parsingError, 'Price/Sales':parsingError, 'Price/Book':parsingError, 'EV/Revenue':parsingError, 'EV/EBITDA':parsingError, 'Price':parsingError}, ignore_index = True)
            print ('Unable to parse: ' + stockName)
            parseSuccessful = False
        #if(parseSuccessful==True):
         #   print ("Showing fundamental data for: " + stockName + "\n", ' Debt/Equity: ' +str(value1), '\t Return on Equity: ' +str(value2), ' Return on Assets: ' +str(value3),
           #        ' Mean Recommendation: ' + str(value4), ' Growth rate: '+str(value5), ' Market Cap: '+str(value6), ' P/E Ratio: '+str(value7), ' PEG Ratio: '+str(value8),
            #       ' Price/Sales: '+str(value9), ' Price/Book: '+str(value10), ' EV/Revenue: '+str(value11), ' EV/EBITDA: '+str(value12), ' Price: '+str(value13))
            
        df.to_csv('C:/Users/Babbu/Desktop/constituents2.csv')

main()
