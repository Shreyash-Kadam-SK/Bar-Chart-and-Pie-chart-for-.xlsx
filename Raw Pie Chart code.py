import matplotlib.pyplot as plt
import pandas as pd

# Read data from the Excel file
file = pd.read_excel('data.xlsx')

# Create a pie chart
plt.pie(file['Value'], labels=file['Label'], autopct='%1.1f%%')
plt.title("Pie Chart from Excel Data")

# Save the chart to a file (e.g., PNG)
plt.savefig('pie_chart.png')

# Display the chart
plt.show()
