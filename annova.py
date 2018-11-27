import pandas as pd
import scipy.stats as st
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
file_path = filedialog.askopenfilename()

df= pd.read_csv(file_path)
n=df.count()
print("Column Count \n",n)

Mean=df.mean()
print("Mean of every column \n",Mean)

variance=df.var()
print("variance of every column \n",variance)

X=sum(df.sum()/sum(n))
print("value of Double X bar is: ",X)

ssb=[]
for i in range(int(len(n))):
    ssb.append(n[i]*(Mean[i]-X)**2)
SSB=sum(ssb)
print("Value of SSB is: ",SSB)


ssw=[]
for i in range(int(len(n))):
    ssw.append((n[i]-1)*variance[i])
SSW=sum(ssw)
print("Value of SSW is: ", SSW)

MSB=SSB/(int(len(n)-1))
print("Value of MSB is: ",MSB)

MSW=SSW/(sum(n)- (int(len(n))))
print("Value of MSW is: ",MSW)

F=MSB/MSW

print("VALUE OF F IS: ",F)


alpha=float(input("Enter value of Alpha "))
P=st.f.ppf(q=1-alpha, dfn=int(len(n)-1), dfd=(sum(n)- (int(len(n)))))
print("Calculated value from F Table is:  ",P)

print()
if P < F:
    print("Reject Null Hypothesis. ")
else:
    print("Fail to Reject Null Hypothesis.")