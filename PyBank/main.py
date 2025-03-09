# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:/Users/mrshw/OneDrive/Desktop/Mod3Challenge/Starter_Code/PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("C:/Users/mrshw/OneDrive/Desktop/Mod3Challenge/Starter_Code/PyBank/Resources/budget_data.csv")  # Output file path

# Define variables to track the financial data
# Add more variables to track other necessary financial data
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Open and read the CSV file
with open(file_to_load, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip the header row
    csv_header = next(csvreader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Track the total and net change
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # Total number of months
        total_months += 1

        # Total net amount of Profit/Losses
        total_pl = total_pl + int(row[1])

    # Calculate the greatest increase in profits (month and amount)
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Calculate the greatest decrease in losses (month and amount)
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Calculate the average net change across the months
    avg_change = sum(profits)/len(profits)
    

# Print the output
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# Generate the output summary
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
