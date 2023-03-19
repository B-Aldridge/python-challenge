# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:26:07 2023

@author: joshu
"""

#code below allows us access to what is on the computer and csv allows us to read/write the format
import os
import csv

#opening csv file from relative path
polldata = "python-challenge/python-challenge/PyPoll/Resources/election_data.csv"

#opening the csv file and reading it
with open(polldata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#this will read the first row/header row
    next(csvreader)
#checking the remaining rows and making a list with the values 
    data = list(csvreader)
#getting the number of rows    
    row_count = len(data)

#getting new list to determine all candidates and who recieved votes
    candi = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candi: 
            candi.append(candidate)
    candicount = len(candi)

#this will calculate the number of votes each candidate recieved as well as the percentage
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candi[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)
        
#this will assign whomever has the most votes as the winner
    winner = votes.index(max(votes))    

#next 8 rows contain how the information will display 
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    
#using a for loop to go over all unique canidates.
    for k in range (0,candicount): 
        print(f"{candi[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candi[winner]}")
    print("----------------------------")    


  
#using relative location and adding a text file to be placed    
    with open("python-challenge/python-challenge/PyPoll/analysisPyPoll.txt","w") as file:

#next 7 rows contain the results from the analysis that will be shown on the text file.
        file.write("Election Results\n") 
        file.write("----------------------------\n")
        file.write(f"Total Votes: {row_count:,}\n") 
        file.write("----------------------------\n")
        for k in range (0,candicount): 
            file.write(f"{candi[k]}: {percentage[k]:.3%} ({votes[k]:,})\n") 
        file.write("----------------------------\n")
        file.write(f"Winner: {candi[winner]}\n") 
        file.write("----------------------------\n") 