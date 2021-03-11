from .MenuInfo import *
from .Chart.Main import *
from .MenuTranslate import *
from .MenuResult import *
from tkinter import Menu
""" 
Можно создать отдельный модуль, где будет
формы для менюшки, чтобы каждый раз не создавать новую
или наследовать. Использовать один код много раз 

Можно ли как-то нормально обновлять приложение?
"""


class App(Tk):
    """Создание приложения"""

    def __init__(self):
        super().__init__()
        menu = Menu(self)
        self.settings()
        menu.add_cascade(label="Таблица", command=self.tableClick)
        menu.add_cascade(label="Графики", command=self.chartClick)
        menu.add_cascade(label="Информация", command=self.infoClick)
        menu.add_cascade(label="Результат", command=self.resultClick)
        menu.add_command(label="Выйти", command=self.destroy)

        self.config(menu=menu)

    def settings(self):
        self.title("Таблица: Продажа домов в округе Кинг, США")
        w = 700
        h = 600
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def tableClick(self):
        self.refresh()
        Table.show(self)

    def chartClick(self):
        self.refresh()
        MainChart.show(self)

    def infoClick(self):
        self.refresh()
        Info.show(self)

    def resultClick(self):
        self.refresh()
        Result.show(self)

    def refresh(self):
        """Обновление приложения"""
        self.destroy()
        App()
