# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:41:03 2022

@author: ASUS
"""

import csv
import numpy as np
import pandas as pd

with open(r"C:\Users\ASUS\Downloads\1080416臺北市各級學校分布圖_28含國小_國中_高中職_特教學校_市立大學_291030730_(1) (3) (2) (1).csv",encoding="ansi") as data:
    readfile =csv.reader(data)
    file = list(readfile)

print(pd.Series(file))
    
# print(file)
# for row in range(len(file)):
#     print(row)
df = pd.DataFrame(file)

print(df.info())

print(df.columns)

print(df.loc[:,1:4])

print(df[[1,3]])

print(df.iloc[:,1:4:2])
# 選出文山區
wen = []

for i in range(len(df)):
    if df.iloc[i,2] == "116":
        wen.append(df.iloc[i,:])

wendata = pd.DataFrame(wen)
print(wendata)


data_group = df.groupby(2)
print(data_group.count())