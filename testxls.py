from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 

file = r'Presidents.xls'
df = pd.read_excel(file)
df.groupby('Political Party')['President'].nunique().plot(kind='bar')
#df.set(xlabel='Political party',ylabel='Years in office',title='America')

plt.show()