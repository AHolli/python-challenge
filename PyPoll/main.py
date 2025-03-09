# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:/Users/mrshw/OneDrive/Desktop/Mod3Challenge/Starter_Code/PyPoll/Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("C:/Users/mrshw/OneDrive/Desktop/Mod3Challenge/Starter_Code/PyPoll/analysis/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
# Define lists and dictionaries to track candidate names and vote counts
# Track the total number of votes cast
candidates = []
num_votes = [] 
percent_votes = [] 
total_votes = 0

# Open the CSV file and process it
with open(file_to_load, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Increment the total vote count for each row 
        total_votes += 1 

        # If the candidate is not already in the candidate list, add them
        # Add a vote to the candidate's count
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Get the vote count and calculate the percentage 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Update the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Generate and print the winning candidate summary
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Save the winning candidate summary to the text file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
