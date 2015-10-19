# Import the linear regression class
from sklearn.linear_model import LinearRegression

from matplotlib import pyplot as plt

import numpy as np

# Initialize the linear regression class.
regressor = LinearRegression()


data = np.genfromtxt('predict.csv', delimiter=',', names=['temp', 'vapour','cloudcover','precipt','years'])

#Two variable Linear Regression to be followed 

predictor = data['precipt']

print type(predictor)

to_predict = data['years']



regressor.fit(predictor[:,np.newaxis],to_predict)

years_to_hotspot = regressor.predict(predictor[:,np.newaxis])

#Plotting the Regressor Line

plt.scatter(predictor,to_predict, color='red')
plt.plot(predictor,regressor.predict(predictor[:,np.newaxis]),color='blue')
plt.show()

print(years_to_hotspot)

mse = sum((to_predict - years_to_hotspot) ** 2)
mse /= len(years_to_hotspot)

print 'Mean Squared Error is:' ,mse




