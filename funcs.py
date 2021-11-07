from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
from datetime import datetime
import glob



def get_df (csvfile):
    df = pd.read_csv(csvfile)
    df.columns = [
    "date",
    "open",
    "high",
    "low",
    "close",
    "RL",
    "closetime",
    "ignore1",
    "ignore2",
    "ignore3",
    "ignore4",
    "ignore5",
    ]
    df = pd.DataFrame(df, columns=["date", "open", "high", "low", "close"])
    lsnumday = []
    lsweekday = []
    lsvar = []
    lst = []
    dictdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    for n in range(len(df)):
        ts = df.iloc[n, 0] / 1000
        dt = datetime.fromtimestamp(ts)
        df.iloc[n, 0] = dt
        weekd = datetime.weekday(df.iloc[n, 0])
        lsnumday.append(weekd)
        var = df.iloc[n, 4] / df.iloc[n, 1] * 100 - 100
        lsvar.append(var)
    for item in lsnumday:
        lsweekday.append(dictdays[item])
    df["weekday"] = lsweekday
    df["variation"] = lsvar
    for n in range(len(df)):
        dtm = df.iloc[n, 0]
        tm = dtm.strftime("%Hh")
        lst.append(tm)
        #print(lst)
    df["opentime"] = lst
    return df

def group_df(folder):
    path = folder
    all_files = glob.glob(path + "/*.csv")
    print(all_files)
    n=0
    df = pd.DataFrame()
    for file in all_files:
        if n == 0:
            df = get_df(file)
            df
            n+=1
        else:
            df2 = get_df(file)
            df = df.append(df2, ignore_index=True)
            
    return df

def gather_infos(df):
    df2 = pd.DataFrame(columns= ["weekday", "opentime", "moy", "med", "ratio", "size", "max", "min"])
    lsweekday = df.weekday.unique().tolist()
    lshours = df.opentime.unique().tolist()
    print(lsweekday)
    print(lshours)
    df3 = df
    df3.index = df.weekday
    x=0
    for day in lsweekday:
        print("searching {}".format(day))
        dfday = df3.filter(like=day, axis=0)
        dfday.index = dfday.opentime
        for hour in lshours:
            lsvar=[]
            pos = 0
            neg = 0
            print("Saecrhing for {}, time :{}".format(day, hour))
            dfhour = dfday.filter(like = hour, axis = 0)
            for n in range(len(dfhour)):
                var = dfhour.iloc[n, 6]
                print(var)
                lsvar.append(var)
                if var >= 0:
                    pos += 1
                else:
                    neg +=1
            print(lsvar)
            echantillon = len(lsvar)
            print("size is {}".format(echantillon))
            mean = round(np.mean(lsvar), 2)
            med = round(np.median(lsvar), 2)
            maxi = round(max(lsvar), 2)
            mini = round(min(lsvar), 2)
            ratio = (((pos/(pos+neg)*100))-50)*2
            print("{} {} {} {}".format(mean, med, ratio, echantillon))
            ls = [day, hour, mean, med, ratio, echantillon, maxi, mini]
            df2.loc[x] = ls
            #print(df2)
            x+=1


    return df2