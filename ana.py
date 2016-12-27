from os import listdir
from os.path import isfile, join
from Tkinter import *
import pandas as pd


# the constructor syntax is:
# OptionMenu(master, variable, *values)
path="data"
stockfiles = [f for f in listdir(path) if isfile(join(path, f))]

master = Tk()

variable = StringVar(master)
variable.set(stockfiles) # default value

menu = apply(OptionMenu, (master, variable) + tuple(stockfiles))
menu.pack()
def get_chart():
    stock = variable.get()
    ext = stock.split('.')[-1]
    file_path = join(path,stock)
    if ext == 'xlsx':
        data = pd.read_excel(file_path,skiprows=1, index_col=0, parse_dates=[0])
        print data
    master.quit()
button = Button(master, text="get chart", command=get_chart)
button.pack()
mainloop()
