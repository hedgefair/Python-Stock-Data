import pandas as pd
import Quandl
import matplotlib.pyplot as plt
import numpy as np

def sp500relative():
    sectorDf = pd.DataFrame.from_csv('C:/Python34/tickersAndSectors.csv')
    sectorDf = sectorDf.fillna("N/A");
    print(sectorDf)
    techTickerList = sectorDf['Information Technology']
    #print(techTickerList)
    for x in techTickerList:
        if(x != 'N/A'):
            print(x+'\n')
            df = Quandl.get("YAHOO/INDEX_GSPC.4", authtoken="KELyNxHx7HZ29257C8jP", trim_start="2015-10-01", returns = "pandas");
            df2 = Quandl.get("WIKI/"+x+".4", authtoken="KELyNxHx7HZ29257C8jP", trim_start="2015-10-01", returns = "pandas")
            #plot_df = df['Close']
            s = df[df.columns[0]]
            s2 = df2[df2.columns[0]]
            s3 = s2/s
            fig = plt.figure()
            fig.subplots_adjust(hspace=.5)
            ax1 = fig.add_subplot(311)
            ax1.plot(s3, label=''+ x + '/sp500 relative')
            ax1.set_title(''+ x + '/sp500 relative')
            ax2 = fig.add_subplot(312)
            ax2.plot(df2, label='aapl')
            ax2.set_title(x + ' close price')
            ax3 = fig.add_subplot(313)
            ax3.plot(df, label='sp500')
            ax3.set_title('sp500 close price')
            
            #ax1.plot(df2, label='aapl')
            #plt.plot(
            #plt.title("my title")
            #plt.legend()
            #plt.legend([ax1, ax2], ['blah1', 'blah2'])
            plt.savefig(x+'.png')
            #print(df);

        else:
            break;
            
    
        
    

sp500relative();
    
