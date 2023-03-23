# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:53:49 2023

@author: joshu
"""
#code below allows us access to what is on the computer and csv allows us to read/write the format
import os
import csv

#declaring path
budget_data_path = "Resources/budget_data.csv"

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Open and read the CSV file
with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        # Track the total number of months
        total_months += 1

        # Track the total profit/loss
        total_profit_loss += int(row[1])

        # Track the change in profit/loss
        current_profit_loss = int(row[1])
        if total_months > 1:
            profit_loss_changes.append(current_profit_loss - previous_profit_loss)
        previous_profit_loss = current_profit_loss

        # Track the months
        months.append(row[0])

# Compute statistics
average_change = sum(profit_loss_changes) / len(profit_loss_changes)
greatest_increase = max(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)+1]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)+1]

# Print results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write results to a text file
with open("analysis/PyBank.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
