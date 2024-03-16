import pandas as pd

df = pd.read_csv("history_mirror.csv",delimiter=",",encoding = "utf-8")
df.dropna()
df["date"] = df["date"].apply(lambda x: x.split("-")[0])
sl = {}
for i in df["date"]:
    if i not in sl:
        sl[i]=1
    else:
        sl[i]+=1
for key, value in sl.items():
    print(f"В {key} году зеркало было использовано {value}")