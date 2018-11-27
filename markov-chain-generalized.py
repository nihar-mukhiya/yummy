# author: NIHAR MUKHIYA
# date: 20/09/2018
# last update: 24/09/2018
# description: Markov chain implementaion in python,
#              where dataset inputted by user in form of csv file.

import tkinter as tk
from tkinter import filedialog
from datascience import *
from pandas import *
import numpy as np

root = tk.Tk()

file_path = filedialog.askopenfilename()
file = Table.read_table(file_path)

a = Table.read_table(file_path)
e = pandas.read_csv(file_path, header = 0)
c = a.num_rows
column_names = a.labels
column = column_names[0]
z = e[column].tolist()
# eset consists of unique column values
eset = list(set(z))
print("unique column values are: ")
print(eset)
print("name of column is: ")
print(column_names)
list = []
i = 0
for x in eset:
    t= a.select(column).where(column, eset[i]).num_rows
    list.append(t)
    i+=1
list2 = []

list2 = list.copy()
for x in range(0, len(list)):
    list2[x] = list2[x] / c
list2 = np.matrix(list2)
list3 = []
w = 0
for x in list:
    list4 = []
    for q in range(0, len(eset)):
        a1 = 0
        for y in range(0, len(z) - 1):
            if(z[y] == eset[w] and z[y + 1] == eset[q]):
                a1+=1
        a1 = a1 / c
        list4.append(a1)
    list3.append(list4)
    w+=1
print(list3)
list3 = np.matrix(list3)
ip = int(input("probability after how many days required? "))
for x in range(1, ip + 1):
    list2 = np.dot(list2, list3)
    print("probability after " +str(x)+ " day is: " + str(list2))
