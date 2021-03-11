from tkinter import Tk
from .Chart import Chart


class MainChart(Tk):
    """Создание окна с данными таблицы"""

    def __init__(self):
        pass

    def show(self):
        Chart.c_btn(self, 4)
