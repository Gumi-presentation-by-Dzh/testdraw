import os
import numpy as np
import scipy
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
xTickMarks = ['R:200ns W:400ns','R:300ns W:400ns','R:400ns W:400ns','R:500ns W:400ns']
x = [1,2,3,4]
N = len(xTickMarks)

Log_data =[[]]
Logfile = ['time.txt']
times=[]
for i in range(len(Logfile)):
    fplog = open(Logfile[i], "r")
    for line in fplog:
        line=line.strip('\t')
        if (line.find('real') != -1):
            times = line.split("real")
            tim = times[1]
            times = tim.split("m")
            second = times[1]
            tim_temp = []
            tim_temp = second.split("s")
            s = float(times[0])*60+float(tim_temp[0])
            Log_data[0].append(s)
print(Log_data[0])

plt.plot(x,Log_data[0],marker='o', markerfacecolor='blue',markersize=12)
plt.ylabel('Memtester 1M runtime')
plt.xticks(x, xTickMarks, rotation=0) 
plt.xlim(0.75, 4.25)
plt.legend()
plt.grid()
plt.show()