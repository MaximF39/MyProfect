from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from pandas import read_csv
import sys, os
import numpy as np

sys.path.insert(0, os.path.abspath('..'))

data = read_csv(r'EuTest\Test.csv')
controlData = read_csv(r'EuTest\СontrolTest.csv')

notCol = ['date', 'price', 'zipcode', 'age', 'long', "yr_built"] # Обучается по всем колонкам кроме
trData = data.drop(notCol, axis=1)
trControlData = controlData.drop(notCol, axis=1)

column = trData.columns # По каким колонкам обучается

X_test = trControlData[column]
Y_test = controlData['price']

X_train = trData[column]
Y_train = data['price']

reg = LinearRegression()

reg.fit(X_train, Y_train) # Обучение
y_pred = reg.predict(X_test) # Предсказывает

#absoluteCorrect = int(100 - mean_absolute_error(Y_test, y_pred))

