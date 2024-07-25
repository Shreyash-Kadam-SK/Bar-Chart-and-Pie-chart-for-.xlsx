import matplotlib.pyplot as plt
import pandas as pd

# Read data from the Excel file
file = pd.read_excel('data.xlsx')
x_axis = file['X values']
y_axis = file['Y values']

# Create a bar chart
plt.bar(x_axis, y_axis, width=0.5)  # You can adjust the width as needed
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Bar Chart from Excel Data")
plt.grid(True)

# Save the chart to a file (e.g., PNG)
plt.savefig('bar_chart.png')

# Display the chart
plt.show()
