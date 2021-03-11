from tkinter import Scrollbar, Tk
from tkinter.ttk import Treeview
from .Way import translate


class Info(Tk):
    """Создание окна с данными таблицы"""

    def __init__(self):
        pass

    def show(self):
        data = translate
        text = data
        parent = None
        self.text = text.columns.values
        self.parent = parent
        self.tree = Treeview(self.parent, columns=self.text[1:], padding='center')
        self.vsby = Scrollbar(parent, orient="vertical", command=self.tree.yview)
        self.vsbx = Scrollbar(parent, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsby.set, xscrollcommand=self.vsbx.set)
        self.vsby.pack(side="right", fill="y")
        self.vsbx.pack(side="bottom", fill="x")
        for i, j in enumerate(self.text):
            if i == 0:
                w = 120
            else:
                w = 560
            self.tree.heading(f"#{i}", text=j)
            self.tree.column(f"#{i}", width=w)
        for i in range(len(text[self.text[0]])):
            self.tree.insert('', 'end', text=text[self.text[0]][i],
                             values=list(map(lambda x: text[x][i], self.text[1:])))
        self.tree.pack(expand=1, fill="y")
