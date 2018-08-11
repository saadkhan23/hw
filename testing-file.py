import sys
print(sys.executable)
print(sys.version)

# plot using matplotlib pyplot
import pandas as pd
import numpy as np
from pandas import DataFrame

sales = pd.read_excel("C:\Users\saadk\Desktop\Saadswork\janfull.xlsx", header=None, names=['Date','Sales'])   #read the csv file (put 'r' before the path string to address any special characters, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
df = pd.DataFrame(sales)
df['Date'] = pd.to_datetime(df['Date'], unit='s')
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
print(sales)
#print(sales.describe())
