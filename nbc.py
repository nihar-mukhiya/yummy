# Author: NIHAR MUKHIYA
# Date: 22/10/2018
# Description: Python implementation of Naive-Bayes classifier.
#              Input is a csv file, class and the constraints of new value to be inserted.
#              Output is the prediction of the class to which the new value with given constraints will belong to!



from pandas import *
import tkinter as tk
from tkinter import filedialog
from datascience import *
import copy

root = tk.Tk()
file_path = filedialog.askopenfilename()
e = pandas.read_csv(file_path, header = 0)
b = Table.read_table(file_path)
number_of_rows = b.num_rows
print(e)
col_names = b.labels
print(col_names)
input1 = int(input("enter the index of column to be selected as class: "))
class_name = col_names[input1]
uniq = e[col_names[input1]].unique()
len_uniq = len(uniq)
class_values = []
numerical_class_values = []

for y in range(len_uniq):
    clas1 = b.select(col_names[input1]).where(col_names[input1], uniq[y]).num_rows
    probs = clas1 / number_of_rows
    class_values.append(probs)
    numerical_class_values.append(clas1)


temp = copy.deepcopy(list(col_names))
temp.remove(temp[input1])
print("enter constraints for each column: ")
collect = []
all_probs = []
for i in range(len(temp)):
    list2 = []
    temp2 = input("for "+temp[i]+": ")
    collect.append(temp2)
    temp3 = b.where(temp[i], collect[i])
    for y in range(0, len_uniq):
        temp4 = 0
        temp4 = temp3.where(class_name, uniq[y]).num_rows
        temp4 = temp4 / numerical_class_values[y]
        list2.append(temp4)
    all_probs.append(list2)
final_probs = []
final_values = {}
for k in range(0, len_uniq):
    temp5 = 1
    for j in range(0, len(all_probs)):
        temp5 = temp5 * all_probs[j][k]
    temp6 = temp5 * class_values[k]
    final_values[uniq[k]] = temp6
print(final_values)
answer = max(final_values, key = final_values.get)
print("According to your given constraints, the new value will belong to class: "+str(answer))