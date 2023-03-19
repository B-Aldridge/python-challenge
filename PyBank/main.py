# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:53:49 2023

@author: joshu
"""
#code below allows us access to what is on the computer and csv allows us to read/write the format
import os
import csv

#opening csv file from relative path
budget_data = ("python-challenge/python-challenge/PyBank/Resources/budget_data.csv")

#declaring variables to use for calculations later
totalmonths = 0
profitloss = 0
value = 0
change = 0
dates = []
profits = []

# opening the csv file and reading it
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#this will read the first row/header row
    csv_header = next(csvreader)

#using csvreader to read the data starting with first row
    first_row = next(csvreader)
#incrementing the variable established earlt to show one more month of data has been read
    totalmonths += 1
#keeping track of the profit and loss for the data
    profitloss += int(first_row[1])
#this will set value with the profit and loss for the first month
    value = int(first_row[1])
    
# starting loop   
    for row in csvreader:
#this will keep track of dates       
        dates.append(row[0])
        
#this will calculate the change on profit and loss from last month to current       
        change = int(row[1])-value
#this will build a list of profit/loss changes for each month
        profits.append(change)
#this will help us calculate change in profit and loss monthly        
        value = int(row[1])
        
#increases the variable by one when one month of data is read       
        totalmonths += 1

#keeping track of total profit and loss for all months        
        profitloss = profitloss + int(row[1])

#this will find the greatest increase in the profit and loss    
    greatest_increase = max(profits)
#this will assign the month with the greatest increase in profit and loss to the greatest_index variable    
    greatest_index = profits.index(greatest_increase)
#setting up the month for the greatest increase   
    greatest_date = dates[greatest_index]
#this will find the greatest decrease in the profit and loss    
    greatest_decrease = min(profits)
#this will assign the month with the greatest decrease in profit and loss to the greatest_decrease variable   
    worst_index = profits.index(greatest_decrease)
#setting up the month for the greatest decrease     
    worst_date = dates[worst_index]

#this calculates the average change regarding the profit and loss per month all time   
    avg_change = sum(profits)/len(profits)
 
#next 7 rows contain how the information will display    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {(totalmonths)}")
print(f"Total: ${(profitloss)}")
print(f"Average Change: ${(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${(greatest_decrease)})")

#using relative location and adding a text file to be placed
with open("python-challenge/python-challenge/PyBank/analysis/PyBank.txt", "w") as file:

#next 7 rows contain the results from the analysis that will be shown on the text file.
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {totalmonths}\n")
    file.write(f"Total: ${profitloss}\n")
    file.write(f"Average Change: ${round(avg_change,2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})\n")
    
