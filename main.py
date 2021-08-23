from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
from datetime import date


root = Tk()
root.title('test')

df = pd.read_csv('data.csv')

df.drop(df.columns[[1,2,3, 5, 6, 8, 17, 18, 19, 20, 21, 22]], axis=1, inplace=True)
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_column',17)

print (df)

df.to_csv('CleanEXM.csv')

def graph():

        plt.style.use('seaborn')

        data = pd.read_csv('CleanEXM.csv')

        data['Created'] = pd.to_datetime(data['Created'])
        data.sort_values('Created', inplace=True)

        price_date = data['Created']
        price_close = data['EUR Value']

        plt.plot_date(price_date, price_close, linestyle='solid', label="NaN values")
        left = date(2020, 5, 15)
        right = date(2020, 7, 15)

        plt.gcf().autofmt_xdate()
        plt.gca().set_xbound(left, right)

        plt.title('Bitcoin Prices')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')

        plt.tight_layout()

        plt.show()

my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()

root.mainloop()