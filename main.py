import pandas as pd
import numpy as np

dataset=pd.read_csv('/content/drive/MyDrive/NFL Play by Play 2009-2017 (v4).csv')
print(dataset.head())
print(dataset.shape[0])
print(dataset.shape[1])



miss_count=dataset.isnull().sum()

print(miss_count[0:10])
print(miss_count.shape)


total_cell=np.product(dataset.shape)
print( total_cell)


total_miss=miss_count.sum()
print(total_miss)


percent_missing_col0 = (miss_count[0]/dataset.shape[0]) * 100
print (percent_missing_col0 , '%')


percent_missing_col4 = (miss_count[4]/dataset.shape[0]) * 100
print (percent_missing_col4 , '%')

print (miss_count[4])


# percent of data that is missing
percent_missing = (total_miss/total_cell) * 100
print(percent_missing, '%')


print (dataset.shape)
dataset2 = dataset.dropna(axis=0)
print (dataset2.shape)
dataset3 = dataset.dropna(axis=1)
print (dataset3.shape)


dataset4 = dataset.fillna(0)
print (dataset.head(10))
print (dataset4.head(10))


dataset5 = dataset.fillna(method='bfill')
print (dataset.head(10))
print (dataset5.head(10))


missing_values_count2 = dataset5.isnull().sum()
print (missing_values_count2)
print ("count2= " , missing_values_count2.sum())


dataset6 = dataset5.fillna(0)
missing_values_count3 = dataset6.isnull().sum()
print (missing_values_count3)
print ("count3= " , missing_values_count3.sum())