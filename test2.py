import tkinter as tk
from tkinter.ttk import Progressbar
import time
from concurrent import futures



class Per():

    def __init__(self, pg, lb):
        self.pg = pg
        self.lb = lb
        self.i = 0
        self.per = tk.StringVar().set(0)
    def test(self,):
        while self.i <= 100:
            #self.pg.configure(value=self.i)
            #self.pg.update()
            self.lb['text'] = str(self.i)
            self.i += 1
            time.sleep(0.02)





root = tk.Tk()

pg = Progressbar(root, orient='horizontal', value=0, maximum=100)
pg.pack()

lb = tk.Label(root)
lb.pack()

b = Per(pg, lb)
b.test()

future_list = []


root.mainloop()