import Graph_Methods as g

while True:
    choice = input("Enter 0 For Bar Chart or 1 for Pie Chart: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 0:
            g.BarChart()
            break
        elif choice == 1:
            g.PieChart()
            break
        else:
            print("Enter 0 or 1 accordingly")
    else:
        print("Enter a integer(number)")

