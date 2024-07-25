import matplotlib.pyplot as plt
import pandas as pd
name = input("Enter File name: ")
value = input("Enter The Value Column name for the Pie Chart: ")
labil = input("Enter The Label Column name for the Pie Chart: ")
title = input("Enter The Title of the Pie Chart: ")

file = pd.read_excel(name)

plt.pie(file[value], labels=file[labil], autopct='%1.1f%%')
plt.title(title)

plt.savefig('pie_chart.png')

plt.show()
