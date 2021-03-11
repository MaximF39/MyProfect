from tkinter import Scrollbar, Tk
from tkinter.ttk import Treeview
"""import sys, os
sys.path.insert(0, os.path.abspath('..'))"""
from .Way import controlData, resLine


class Table(Tk):
    """Создание окна с данными таблицы"""

    def __init__(self):
        pass

    def show(self):
        parent = None
        text = controlData
        self.text = text.columns.values
        self.parent = parent
        self.tree = Treeview(self.parent, columns=self.text[1:])
        self.vsby = Scrollbar(parent, orient="vertical", command=self.tree.yview)
        self.vsbx = Scrollbar(parent, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsby.set, xscrollcommand=self.vsbx.set)
        self.vsby.pack(side="right", fill="y")
        self.vsbx.pack(side="bottom", fill="x")
        for i, j in enumerate(self.text):
            self.tree.heading(f"#{i}", text=j)
            self.tree.column(f"#{i}", width=100, anchor="s")
        for i in range(len(text[0:resLine])): # Вывод всех строк range(len(text[self.text[0:]]))
            self.tree.insert('', 'end', text=text[self.text[0]][i],
                             values=list(map(lambda x: text[x][i], self.text[1:])))
        self.tree.pack(expand=1, fill="y")
