#Script to generate random dataset with annual temperature
import pandas as pd


import csv

import random

from pandas import DataFrame,read_csv


months = ['Jan','Feb','March','April','May','June','July','August','September','October','November','December']

temp = []

count = 1

while (count<=12):
	rand_temp = random.random() + random.randint(16,30)
	temp.append(rand_temp)
	count = count + 1

dataset = zip(months,temp)

df = pd.DataFrame(data=dataset,columns=['Months','Temperature'])

df.to_csv('randomdataset.csv',index=False,header=False)

# Do similiarly for all parameters

# For simplicity,make this as a function and call when required

#Function to generate random dataset

def random_dataset(low_range,high_range,parameter):
	months = ['Jan','Feb','March','April','May','June','July','August','September','October','November','December']

	temp = []

	count = 1

	while (count<=12):
		rand_temp = random.random() + random.randint(low_range,high_range)
		temp.append(rand_temp)
		count = count + 1

	dataset = zip(months,temp)

	df = pd.DataFrame(data=dataset,columns=['Months',parameter])

	df.to_csv('randomdataset'+parameter+'.csv',index=False,header=False)

def random_dataset_for_prediction(records,parameter='default'):
	
	#generate records rows of sample data

	count = 0

	data = []
	while count<records:
		
		row = []
		rand_temp = random.random() + random.randint(16,30)
		rand_precipt = random.randint(100,150)
		rand_vapour = random.randint(120,200)
		rand_cloud_cover = random.randint(200,250)
		years = random.randint(5,10)
		row.append(rand_temp)
		row.append(rand_vapour)
		row.append(rand_cloud_cover)
		row.append(rand_precipt)
		row.append(years)
		data.append(row)

		count = count + 1 

	with open('predict.csv', 'wb') as f:
		wtr = csv.writer(f)
		wtr.writerows(data)
		

#function_call
random_dataset_for_prediction(20)