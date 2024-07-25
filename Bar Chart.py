import matplotlib.pyplot as plt
import pandas as pd
name = input("Enter File name: ")
xaxis = input("Enter The X-Axis Column name for the Bar Chart: ")
yaxis = input("Enter The Y-Axis Column name for the Bar Chart: ")
title = input("Enter The Title of the Bar Chart: ")

file = pd.read_excel(name)
x_axis = file[xaxis]
y_axis = file[yaxis]

plt.bar(x_axis, y_axis, width=0.5)
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.title(title)
plt.grid(True)

plt.savefig('bar_chart.png')

plt.show()
