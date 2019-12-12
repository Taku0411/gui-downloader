import tkinter as tk
from tkinter.ttk import Progressbar
import time

root = tk.Tk()
pg = Progressbar(root, orient='horizontal', value=0, maximum=100)
pg.pack()
i =1
while i <= 100:
    pg.configure(value=i)
    pg.update()
    i += 1
    time.sleep(0.02)
root.mainloop()