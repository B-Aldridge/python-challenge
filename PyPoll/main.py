# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:26:07 2023

@author: joshu
"""
#importing modules
import os
import csv

# Set file path
polldata = "https://raw.githubusercontent.com/B-Aldridge/python-challenge/main/PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""

# Read in data and perform analysis
with open(polldata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Loop over each row in data
    for row in csvreader:
        # Increment total vote count
        total_votes += 1
        
        # Add candidate to dictionary if not already in it
        if row[2] not in candidates:
            candidates[row[2]] = 0
        
        # Increment vote count for candidate
        candidates[row[2]] += 1
    
    # Determine winner using candidate dictionary
    winner = max(candidates, key=candidates.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes:,}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = votes/total_votes*100
    print(f"{candidate}: {percentage:.3f}% ({votes:,})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write results to text file
output_path = os.path.join("output", "PyPoll.txt")
with open(output_path, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes:,}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = votes/total_votes*100
        file.write(f"{candidate}: {percentage:.3f}% ({votes:,})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
