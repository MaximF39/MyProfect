from pandas import read_csv
import sys
from os.path import abspath
sys.path.insert(0, abspath('..'))

sys.path.insert(0, abspath('..'))

resLine = 50

controlData = read_csv(r'EuTest\СontrolTest.csv')
translate = read_csv(r'EuTest\Translate.csv', sep=':')
controlResult = read_csv(r'EuTest\СontrolResult.csv')


data = read_csv(r'EuTest\test.csv') # Chart для графиков
