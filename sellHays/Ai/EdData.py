import pandas as pd
import numpy as np

controlTest = pd.read_csv(r'EuTest\СontrolTest.csv')

controlTest['price'] = controlTest['price'].apply(np.int64)
controlTest['age'] = controlTest['yr_built'].max() - controlTest['yr_built']  # Возраст зданий на момент продажи
controlTest['lat'] = controlTest['lat'].apply(np.float16, 1)
controlTest['long'] = controlTest['long'].apply(np.float16, 1)
controlTest['date'] = pd.to_datetime(controlTest['date']).dt.date
controlTest.to_csv(r'EuTest\СontrolTest.csv', index=False)

data = pd.read_csv(r'EuTest\Test.csv')
data['price'] = data['price'].apply(np.int64)
data['age'] = data['yr_built'].max() - data['yr_built']  # Возраст зданий на момент продажи
data['lat'] = data['lat'].apply(np.float16, 1)
data['long'] = data['long'].apply(np.float16, 1)
data['date'] = pd.to_datetime(data['date']).dt.date
data.to_csv(r'EuTest\Test.csv', index=False)
