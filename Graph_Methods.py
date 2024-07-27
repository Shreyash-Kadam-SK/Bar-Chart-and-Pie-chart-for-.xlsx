import matplotlib.pyplot as plt
import pandas as pd
import os


def BarChart():
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

    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.savefig(os.path.join(output_dir, 'bar_chart.png'))

    plt.show()

def PieChart():
    name = input("Enter File name: ")
    labil = input("Enter The Label Column name for the Pie Chart: ")
    value = input("Enter The Value Column name for the Pie Chart: ")
    title = input("Enter The Title of the Pie Chart: ")

    file = pd.read_excel(name)

    plt.pie(file[value], labels=file[labil], autopct='%1.1f%%')
    plt.title(title)

    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.savefig(os.path.join(output_dir, 'pie_chart.png'))

    plt.show()

