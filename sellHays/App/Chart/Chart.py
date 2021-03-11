import matplotlib.pyplot as plt #figure,
from tkinter import Button
import seaborn as sns #heatmap
from ..Way import data


class Chart():
    """Рисует графики по запросу кнопки"""

    def __init__(self):
        pass

    def c_btn(self, count):
        """Создание и информация куда ведёт"""
        def allG():
            plt.figure(figsize=(12, 8))
            sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',fmt='.2f')
            plt.title('Зависимость каждого аргумента от другого')
            plt.tight_layout()
            plt.show()

        def depen():
            column = ['bedrooms', 'floors', 'waterfront', 'view', 'grade'] #
            fig, axs = plt.subplots(5, 2, figsize=(12, 8))
            for i, clm in enumerate(column):
                sns.countplot(x=data[clm], ax=axs[i][0])
                sns.boxplot(x=data[clm], y=data['price'], ax=axs[i][1])
            plt.tight_layout()
            plt.show()

        def price_map():
            fig, ax = plt.subplots(figsize=(16, 5))
            plt.scatter(data['lat'], data['long'], c=data['price'], cmap='RdYlBu_r', vmax=data['price'].max() / 2)
            ax.set_title('Карта по цене')
            plt.xlabel('Lattitude')
            plt.ylabel('Longtitude')
            plt.colorbar()
            plt.show()

        def water_map():
            fig, ax = plt.subplots(figsize=(16, 5))
            plt.scatter(data['lat'], data['long'], c=data['waterfront'], cmap='RdBu_r')
            ax.set_title('Карта по выходу к воду')
            plt.xlabel('Lattitude')
            plt.ylabel('Longtitude')
            plt.colorbar()
            plt.show()

        x = 10
        y = 20
        # Можно создать отдельный файл, откуда будут читаться название кнопки и её действие
        infoBtn = [['Картина зависимости', 'Основная зависимость', 'Карта по цене', 'Карта по воде'],
                   [allG, depen, price_map, water_map]]
        for i in range(count):
            self.btn = Button(text=infoBtn[0][i], background="#555", foreground="#ccc",
                                 padx="1", pady="1", font="1", command=infoBtn[1][i], width=24)
            self.btn.place(x=x, y=y)
            y += 40
