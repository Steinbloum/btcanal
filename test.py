import pandas as pd
from datetime import datetime as dt
import numpy as np



df = pd.read_csv("BTCdaily.csv")
print(df)

def setup():
    global df
    ls = []
    for n in range(len(df)):
        datestr = df.iloc[n, 0]
        #print(datestr)
        dateobj = dt.strptime(datestr, '%Y-%m-%d %H:%M:%S')
        df.iat[n, 0] = dateobj
        
        weekd = dt.weekday(dateobj)
        ls.append(weekd)
    df['weekday'] = ls
    df['var'] = df['close'] / df['open'] * 100 -100
    #print(df)
    dictdays = {
        0:'Monday',
        1:'Tuesday',
        2:'Wednesday',
        3:'Thursday',
        4:'Friday',
        5:'Saturday',
        6:'Sunday'
    }
    ls = []
    for n in range(len(df)):
        numday = df.iloc[n, 6]
        weekday = dictdays[numday]
        ls.append(weekday)
    df['weekday'] = ls
    print(df)

def by_weekday():
    lsday = df['weekday'].unique().tolist()
    print(lsday)
    print(df)
    dicta = {}
    
    for day in lsday:
        ls=[]
        x=0
        for n in range(len(df)):
            if df.iloc[n, 7] > 0:
                if day == df.iloc[n, 6]:
                    while x <= 93 : 
                        vari = round(df.iloc[n, 7], 3)
                        #print(vari)
                        #print(type(vari))
                        
                        ls.append(vari)
                        x+=1
                        n+=1
        print('{} lenght is {}'.format(day, len(ls)))
        dicta[day] = ls
    #print(dicta)
    data = dicta
    df2 = pd.DataFrame.from_dict(data)
    data2 = {}
    for key, value in dicta.items():
        dicta[key] = round(np.average(value), 2)
    
    data = dicta
    print(data)
    df3 = pd.DataFrame(data, index=[0])
    print(df2)
    print(df3)



setup()
by_weekday()
print(df)
