import sys
print(sys.executable)
print(sys.version)

# plot using matplotlib pyplot
import pandas as pd
import numpy as np
import holtwinters as hw
import csv
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline
matplotlib.style.use('ggplot')
from datetime import datetime as dt
from math import sqrt
from operator import add
from pandas import DataFrame

with open ("C:\Users\saadk\Desktop\Saadswork\janfull.csv", 'rU') as f:
    reader = csv.reader(f)
    col_names = reader.next()
    rows = [(dt.strptime(row[0], '%y-%b'), float(row[1])) for row in reader]
sales_df = pd.DataFrame(rows, columns = col_names)
raw_ls = list(sales_df['sales'])

# optimized parameters
hw_fc, alpha, beta, rmse = hw.linear(raw_ls,3)

print "alpha:%s, beta:%s" %(alpha, beta)
print "rmse: %s, frac_rmse: %s" %(rmse, rmse/np.mean(raw_ls))

plt.plot(raw_ls, color = 'red', marker = 'o', markersize = 4)
plt.plot([None]*(len(raw_ls)-1) + [raw_ls[-1]] + hw_fc, color = 'blue', marker = 'o', alpha=.4)















#sales = pd.read_excel("C:\Users\saadk\Desktop\Saadswork\janfull.xlsx", header=None, names=['Date','Sales'])   #read the csv file (put 'r' before the path string to address any special characters, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
#df = pd.DataFrame(sales)
#df['Date'] = pd.to_datetime(df['Date'], unit='s')
#df = DataFrame(sales,columns=['Date','Sales'])    # assign column names
#print (df)

#dataColumns = ['Date', 'Sales']
#sales = pd.read_csv('C:\Users\saadk\Desktop\Saadswork\janfull.csv', sep='\t', header=None)
#df = pd.DataFrame(sales, columns = dataColumns)

#sales.index = pd.to_datetime(sales.index)

#sales.plot()
#sales.plot()
#plt.show()
#print(sales.describe())
#print(sales)
#print(sales.describe())
