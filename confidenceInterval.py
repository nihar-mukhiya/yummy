from scipy import stats
import math
from tkinter import *


def calculate_tc():
    typecasted = list(map(int, textTc.get().split(',')))

    confidence_interval = typecasted[0]
    n = typecasted[1]
    conf_inter = confidence_interval / 100
    df = n - 1
    print("Simple Tc : ", stats.t.ppf(conf_inter, df))


def calculate_pop_variance_sd():
    typecasted = list(map(float, textVarSd.get().split(',')))
    df = typecasted[2] - 1
    confidence_interval = typecasted[0]
    sd_sqr = typecasted[1] ** 2

    rhs = (1 - (confidence_interval / 100)) / 2
    lhs = (1 + (confidence_interval / 100)) / 2

    rhs = round(stats.chi2.isf(rhs, df), 3)
    lhs = round(stats.chi2.isf(lhs, df), 3)

    print("Area to Left : ", lhs, " and RHS : ", rhs)

    right_conf = (df * sd_sqr) / rhs
    left_conf = (df * sd_sqr) / lhs
    print("Confidence Interval for Variance : {0} < {1} < {2}".format(right_conf, sd_sqr, left_conf))

    right_sd_conf = math.sqrt(right_conf)
    left_sd_conf = math.sqrt(left_conf)
    print("Confidence Interval for SD : {0} < {1} < {2}".format(right_sd_conf, sd_sqr, left_sd_conf))


def calculate_population_mean():
    typecasted = list(map(int, textErr.get().split(',')))

    confidence_interval = 1 - (typecasted[0] / 100)
    confidence_interval = confidence_interval / 2
    df = typecasted[3] - 1
    mean = typecasted[2]

    confidence_interval = round(confidence_interval, 3)
    tc = stats.t.ppf(confidence_interval, df)

    e = tc * (typecasted[1] / math.sqrt(typecasted[3]))
    print("Error for Population Mean is : ", abs(e))
    print("Confidence Interval : {0} < {1} < {2}".format(mean + e, mean, mean - e))


def calculate_pop_proportion():
    typecasted = list(map(int, textPop.get().split(',')))
    confidence_interval = typecasted[0]
    x = typecasted[1]
    n = typecasted[2]

    p_hat = round(x / n, 3)
    q_hat = round(1 - p_hat, 3)
    area = 1 - (confidence_interval / 100)
    area = area / 2
    Zc = abs(stats.norm.ppf(area))
    Zc = round(Zc, 2)

    product = (p_hat * q_hat) / n
    e = Zc * math.sqrt(product)
    e = round(e, 4)
    print("Error for Population Proportion is :", abs(e))
    print("Confidence Interval : {0} < {1} < {2}".format(p_hat - e, p_hat, p_hat + e))


root = Tk()
root.title("Confidence Intervals")

Label(root, text="Enter Confidence Interval and N : ").grid(row=1, column=0, sticky=W)
textTc = StringVar()
Entry(root, textvariable=textTc).grid(row=1, column=1, sticky=W)
Button(root, text="Calculate Simple Tc", command=calculate_tc).grid(row=2, column=1, sticky=W)

Label(root, text="Enter Confidence Interval , s , mean and n : ").grid(row=3, column=0, sticky=W)
textErr = StringVar()
Entry(root, textvariable=textErr).grid(row=3, column=1, sticky=W)
Button(root, text="Calculate Population Mean", command=calculate_population_mean).grid(row=4, column=1, sticky=W)

Label(root, text="Enter Confidence Interval , x and n : ").grid(row=5, column=0, sticky=W)
textPop = StringVar()
Entry(root, textvariable=textPop).grid(row=5, column=1, sticky=W)
Button(root, text="Calculate Population Proportion", command=calculate_pop_proportion).grid(row=6, column=1, sticky=W)

Label(root, text="Enter Confidence Interval , sd and n :").grid(row=7, column=0, sticky=W)
textVarSd = StringVar()
Entry(root, textvariable=textVarSd).grid(row=7, column=1, sticky=W)
Button(root, text="Calculate Population Variance and SD", command=calculate_pop_variance_sd).grid(row=8, column=1,
                                                                                                  sticky=W)

root.mainloop()