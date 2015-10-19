from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

from numpy import arange

from datasetcreate import random_dataset_for_prediction

from chartgen import scatterplot,barplot,histplot,barchart

import bisect

import numpy as np 


regressor = LinearRegression()

import pandas


guj = pandas.read_csv("randomdataset.csv")

#nextday = guj["Year"].iloc[1:]

print guj.columns

#plt.plot(guj['Jan'],guj['Feb'])
#plt.show()


# To generate different kind of plots using the CSV File

data = np.genfromtxt('randomdataset.csv', delimiter=',', names=['x', 'y'])

print data['y']

#Line Plot
months = [0,1,2,3,4,5,6,7,8,9,10,11]

plt.plot(months, data['y'], color='r', label='the data')
plt.title("Plot : Months vs Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature")


plt.show()

#Histogram
'''
temp_integer = [int(number) for number in data['y']]

print temp_integer

n, bins, patches = plt.hist(temp_integer, 50, normed=1, facecolor='green', alpha=0.75)
plt.title("Histogram")
plt.xlabel("Months")
plt.ylabel("Temperature")
'''

#Scatterplot
temp_integer = [int(number) for number in data['y']]


#Calling from chartgen
scatterplot(months,temp_integer)
barplot(months,temp_integer)
histplot(temp_integer)
barchart(months,temp_integer)


