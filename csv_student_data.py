import pandas as pd
import csv

# demo_data.csvをデータフレーム(df)として読み込む
df=pd.read_csv("demo_data.csv")

# 新規ファイル(student_data.csv)の為の列名定義
header =  ["id","time","temp"]

with open("student_data.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(header)


for number,i in enumerate(range(0,len(df)),1):
    # 学籍番号を任意の行、0列目を参照
    student_id=df.iloc[i,0]
    # 時間を任意の行、1列目を参照
    time=df.iloc[i,1]
    # 体温を任意の行、2列目を参照
    temp=df.iloc[i,2]
    # 体温が37.5度以上だったら、新規ファイル(student_data.csv)に追加
    if temp>=37.5:
        
        body =[[student_id,time,temp]]
        with open("student_data.csv","a") as f:
            writer=csv.writer(f)
            writer.writerows(body)