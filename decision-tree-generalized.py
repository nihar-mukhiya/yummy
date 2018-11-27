# Author: Nihar Mukhiya
# Date: 28/09/2018
# Last update: 30/09/2018
# Description: A python implementation of finding root procedure of decision tree.
#              User gives input from csv file and has choice to make a particular column of csv as
#              'class' of the finding root procedure in decision tree.
#              User is displayed the column name chosen as the root of decision tree.
import tkinter as tk
from tkinter import filedialog
from datascience import *
from pandas import *
import copy
import numpy as np
from math import log2

def ent(list):
    entropy, g = 0, 0
    for z in list:
        entropy = entropy + (- list[g] * log2(list[g]))
        g+=1
    return entropy

root = tk.Tk()

file_path = filedialog.askopenfilename()
file = Table.read_table(file_path)
a = Table.read_table(file_path)
e = pandas.read_csv(file_path, header = 0)
c = a.num_rows
column_names = a.labels
print("Column names in your csv are: ")
i = 1
for x in range(0, len(column_names)):
    print(str(i)+ ".", column_names[x])
    i+=1

clas = int(input("select the column to be selected as class: "))
#uniq contains unique values in our class
uniq = e[column_names[clas - 1]].unique()
l = len(uniq)
# p_class will contain probabilities of values in our selected class column
p_class = []

for y in range(0, len(uniq)):
    clas1 = a.select(column_names[clas - 1]).where(column_names[clas - 1], uniq[y]).num_rows
    clas1 = clas1 / c
    p_class.append(clas1)

entropy_val = ent(p_class)
print("\nEntropy for your class is: " +str(entropy_val)+ "\n")
temp = copy.deepcopy(list(column_names))
temp.remove(temp[clas - 1])
prob_of_column = {}
prob_of_values_in_column = {}
info = {}
temp2 = []
for z in range(0, len(temp)):
    uniq1 = e[temp[z]].unique()

    clas3 = []

    clas5 = []
    for y in range(0, len(uniq1)):
        clas4 = []
        clas5 = a.where(temp[z], uniq1[y])
        clas2 = a.select(temp[z]).where(temp[z], uniq1[y]).num_rows
        val = clas2
        clas2 = clas2 / c
        clas3.append(clas2)
        for b in range(0, len(uniq)):
            temp1 = clas5.where(column_names[clas - 1], uniq[b]).num_rows
            temp1 = temp1 / val
            clas4.append(temp1)
            prob_of_values_in_column[uniq1[y]] = clas4
    prob_of_column[temp[z]] = clas3

    templist = []
    for h in range(0, len(prob_of_column[temp[z]])):
            temp5 = 0
            j1 = prob_of_column[temp[z]][h]
            temp4 = 0
            for h2 in range(0, len(uniq)):
                j2 = prob_of_values_in_column[uniq1[h]][h2]
                try:
                    temp5 = temp5 + (-(j2 * log2(j2)))
                except ValueError:
                    temp5 = 0
                temp4 = j1 * temp5
            templist.append(temp4)
    sum1 = sum(templist)
    sum1 = entropy_val - sum1
    info[temp[z]] = sum1
print("Values of info gain of all the columns are: \n")
print(info)
root = max(info, key=info.get)
print("\nRoot of the decision tree is: " +str(root))












