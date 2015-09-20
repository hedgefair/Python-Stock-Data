#Ambarish Gugilla
#Stock Analysis project
#Sep 12, 2015
#This script parses HTML data from the Wikipedia S&P500 List of Stocks.
#It gets the ticker symbol and its associated sector. Some unnecessary
#use of pandas dataframe is involved, but was used for practice. Returns a
#final dictionary which holds each sector and its list of tickers.


import requests
import pandas as pd
import re
import math

def get_sectors():
    r = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    text = str(r.text)
    someList = []
    tickerList = []  
    sectorBlah = []
    sectorDict = {}
    text = text.replace('http://www.nasdaq.com/symbol/', 'https://www.nyse.com/quote/XNYS:')
    splitList = text.split('https://www.nyse.com/quote/XNYS:')

    for x in range(1, len(splitList)):
        tickerSymbol = splitList[x].split('">')[0]
        try:
            sector = splitList[x].split('reports')[1].split('</a></td>')[1].split('</td>')[0]
            someList.append(sector)
            tickerList.append(tickerSymbol)
            city = sector.split('title="')[1].split('">')[0]
            try:
                city = city.split('"')[0]
                print("wtf")
                print(city)
            except:
                pass
        except Exception as e:
            pass

    sectorList=['Industrials', 'Health Care', 'Information Technology', 'Financials', 'Consumer Discretionary',
                          'Utilities', 'Materials', 'Energy', 'Consumer Staples', 'Telecommunications Services']
   
    df = pd.DataFrame(columns=['Industrials', 'Health Care', 'Information Technology', 'Financials', 'Consumer Discretionary',
                          'Utilities', 'Materials', 'Energy', 'Consumer Staples', 'Telecommunications Services'])

    sectorDirectory =  []
    print("DAMN!!")
    for x in range(0, len(someList)):
        someList[x] = someList[x].split('>')[1]
        sectorDict.update({tickerList[x]:someList[x]})
        categ = str(someList[x])
        df = df.append({categ: tickerList[x]}, ignore_index = True)
        
    for i in range(0, len(sectorList)):
        sectorDirectory.append(df[sectorList[i]].tolist())
       
    finalDict = {}
    
    for x in range (0, len(sectorList)):
        q = sectorDirectory[x][:]
        q[:] = (value for value in q if str(value) != 'nan')
        sectorDirectory[x] = q
        finalDict.update({sectorList[x]: sectorDirectory[x]})
        
            
    print(finalDict)



def 

get_sectors()