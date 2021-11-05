import pandas as pd
from datetime import datetime


df = pd.read_csv("BTCUSDT-1h-2021-10.csv")
df.columns = [
    "opentime",
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
df = pd.DataFrame(df, columns=["opentime", "open", "high", "low", "close"])
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
    tm = dtm.time()
    lst.append(tm)
df["opentime"] = lst
print(df)
