from pandas import *
import tkinter as tk
from tkinter import filedialog
from math import sqrt
from scipy import stats
from datascience import *
import copy
root = tk.Tk()
file_path = filedialog.askopenfilename()
e = pandas.read_csv(file_path, header = 0)
a = Table.read_table(file_path)
print("your input table is: ")
print(a)

col_names = list(a.labels)
temp2 = copy.deepcopy(list(col_names))
col_names.remove(col_names[-1])
inputter = []
collect = []
final_values = []
for i in range(len(col_names)):
    temp1 = int(input("enter value for "+str(col_names[i])+":"))
    inputter.append(temp1)
for y in range(len(e.index)):
    temp = 0
    for z in range(len(col_names)):
        temp = temp + ((inputter[z] - int(e.iloc[y][z]))**2)
    temp3 = []
    temp = sqrt(temp)
    temp3.extend((temp, e.iloc[y][len(temp2) - 1]))
    collect.append(temp)
    final_values.append(temp3)

input_k = int(input("enter k: "))

sorted(collect)
list2 = collect[0: input_k]
list3 = []
for m in range(len(list2)):
    list3.append(final_values[m][1])
common = max(set(list3), key=list3.count)
print("the class values of your "+str(input_k)+ " nearest neighbours are: ")
print(list3)
print("your entry belongs to class: " +common)
