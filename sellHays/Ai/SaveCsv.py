import pandas as pd
import numpy as np
from Ai.EdData import *
import sys, os
sys.path.insert(0, os.path.abspath('..'))

import Ai.Main

controlResult = pd.read_csv(r'EuTest\СontrolTest.csv')
resLine = len(controlResult['price'])
predictPrice = np.array(Ai.Main.y_pred, dtype=int)
error = []
for i in range(resLine):
    if predictPrice[i] >= controlResult['price'][i]:  # 200 150 0.25 200 - 150 / 200
        error.append(int(abs((controlResult['price'][i] - predictPrice[i])/controlResult['price'][i] * 100)))
    else:  # 150 200 1 / 3
        error.append(int(abs((controlResult['price'][i] - predictPrice[i])/controlResult['price'][i] * 100)))

correct = np.array(error)
# Ниже код не убираю с if else, ибо не понимаю, почему ошибка вылазит
if 'error' in controlResult.columns:
    controlResult = controlResult.drop(['error', 'predict_price'], axis=1)

if not ('error' in controlResult.columns):
    controlResult.insert(3, "predict_price", predictPrice, True)
    controlResult.insert(4, "error", error, True)
else:
    controlResult['predict_price'] = predictPrice
    controlResult['error'] = error

controlResult = controlResult.sort_values(['error'], ascending=False, kind='mergesort')
controlResult.to_csv(r'EuTest\СontrolResult.csv', index=False)

