# 参考サイト:https://excel-ubara.com/python/python022.html

import csv

file_name=r"student_data.csv"

csv_list=[["学籍番号","名字","名前","欠席理由"]]

with open(file_name,"w",encoding="utf-8") as obj:
    writer = csv.writer(obj, lineterminator="\n")
    for r in csv_list:
        writer.writerow(r)