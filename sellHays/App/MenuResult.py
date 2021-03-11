# импортировать из файла техтРезульт
from tkinter import Scrollbar, Tk, Label
from tkinter.ttk import Treeview
import sys
from os.path import abspath
sys.path.insert(0, abspath('..'))
from .Way import controlResult, resLine

class Result(Tk):
    """Создание окна с данными таблицы"""

    def __init__(self):
        pass

    def show(self):
        text = controlResult
        parent = None
        self.text = text.columns.values
        self.parent = parent
        self.tree = Treeview(self.parent, columns=self.text[1:])
        self.vsby = Scrollbar(parent, orient="vertical", command=self.tree.yview)
        self.vsbx = Scrollbar(parent, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsby.set, xscrollcommand=self.vsbx.set)
        self.vsby.pack(side="right", fill="y")
        self.vsbx.pack(side="bottom", fill="x")
        txtAbsCor = absCor()
        self.absCorect = Label(text="Средняя\nпогрешность равна:\n" + txtAbsCor)
        self.absCorect.place(x=500, y=200)
        for i, j in enumerate(self.text):
            self.tree.heading(f"#{i}", text=j)
            self.tree.column(f"#{i}", width=100, anchor="s")
        for i in range(len(text[0:resLine])):  # Вывод всех строк range(len(text[self.text[0:]]))
            self.tree.insert('', 'end', text=text[self.text[0]][i],
                             values=list(map(lambda x: text[x][i], self.text[1:])))
        self.tree.pack(expand=1, fill="y")

def train():
    None

def absCor():
    from pandas import read_csv
    textResult = read_csv(r'EuTest\СontrolResult.csv')
    textAbsCor = 0
    for i in textResult['error']:
        textAbsCor += i
    textAbsCor = str("{0:.2f}".format(textAbsCor / len(textResult)))

    return textAbsCor + '%'


if __name__ == '__main__':
    print(absCor())
