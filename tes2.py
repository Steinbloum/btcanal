import pandas as pd
from datetime import datetime as dt

#initialise
df = pd.read_csv('BTCdaily.csv')
print(df)

#Convert days
df['var'] = round(df['close']/df['open'] * 100 -100, 3)
print(df)
ls = []
for n in range(len(df)):
    datestr = df.iloc[n, 0]
    #print(datestr)
    dateobj = dt.strptime(datestr, '%Y-%m-%d %H:%M:%S')
    df.iat[n, 0] = dateobj
    
    weekd = dt.weekday(dateobj)
    ls.append(weekd)
df['weekday'] = ls
print(df)
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
    numday = df.iloc[n, 7]
    weekday = dictdays[numday]
    ls.append(weekday)
df['weekday'] = ls
print(df)

#calculate and make a new frame
lsday = df['weekday'].unique().tolist()
dictapos = {}
dicctaneg = {}
for day in lsday:
    lspos = []
    lsneg = []
    x=0
    for n in range(len(df)):
        if day == df.iloc[n, 7]:
            if df.iloc[n, 6] >0:
                while x <= 93:
                    print('{}, {} is positive'.format(day, df.iloc[n, 6]))
                    lspos.append(round(df.iloc[n, 6],2))
                    x+=1
                    n+=1
                
            if df.iloc[n, 6] <=0:
                while x <= 93:
                    print('{}, {} is positive'.format(day, df.iloc[n, 6]))
                    lsneg.append(round(df.iloc[n, 6],2))
                    x+=1
                    n+=1
        dictapos[day] = lspos
        dicctaneg[day] = lsneg
        

dfpos = pd.DataFrame.from_dict(dictapos)
dfneg = pd.DataFrame.from_dict(dicctaneg)

print(dfpos)
print(dfneg)
