import pandas as pd
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

df=pd.read_csv("demo_data.csv")

for number,i in enumerate(range(0,len(df)),1):
    student_id=df.iloc[i,0]
    time=df.iloc[i,1]
    temp=df.iloc[i,2]
    if temp>=37.5:
        pass