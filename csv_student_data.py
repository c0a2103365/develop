import pandas as pd
import csv

df=pd.read_csv("demo_data.csv")

header =  ["id","time","temp"]

with open("student_data.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(header)


for number,i in enumerate(range(0,len(df)),1):
    student_id=df.iloc[i,0]
    time=df.iloc[i,1]
    temp=df.iloc[i,2]
    if temp>=37.5:
        
        body =[[student_id,time,temp]]
        with open("student_data.csv","a") as f:
            writer=csv.writer(f)
            writer.writerows(body)