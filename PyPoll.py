# Data we need to retrieve.
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote


import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("DataBootcamp/Week-3-Python/ElectionAnalysis/Resources", "election_results.csv")

# create filename variable to write file
file_to_save = os.path.join("DataBootcamp/Week-3-Python/ElectionAnalysis/analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

     #to do: read and analyze data here
     #read the file object with the reader fxn.
     file_reader = csv.reader(election_data)

     #print each row in the csv file
     for row in file_reader:
          print(row)
