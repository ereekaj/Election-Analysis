# Election-Analysis

## Overview of Election Audit: 
I've already been working with the Colorado Board of Elections to complete an audit of one of their elections. The results have been submitted but now the election commission has requested some additional data to complete the audit.  The purpose of this election audit analysis will be to use the same data used in the previous audit to determine the following information:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Election-Audit Results: 
The screenshot below shows the results of the election audit in the terminal. These results can also be found in the text file [Election_Analysis.txt](https://github.com/ereekaj/Election-Analysis/blob/main/analysis/election_analysis.txt).
![ScreenshotTerminal](https://github.com/ereekaj/Election-Analysis/blob/main/Resources/ScreenshotTerminal.png)

- *How many votes were cast in this congressional election?* In this election, 369,711 votes were cast. 

- *Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.* A breakdown of the total number and percentage of votes per county is shown below:
  - Jefferson: 10.5% (38,855 votes)
  - Denver: 82.8% (306,055 votes)
  - Arapahoe: 6.7% (24,801 votes)

- *Which county had the largest number of votes?* Denver County had the largest number of votes which resulted in 82.8% of the total votes. 

- *Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.* A breakdown of the total number and percentage of votes per candidate is shown below:
  - Charles Casper Stockham: 23.0% (85,213 votes)
  - Diana DeGette: 73.8% (272,892 votes)
  - Raymon Anthony Doane: 3.1% (11,606 votes) 

- *Which candidate won the election, what was their vote count, and what was their percentage of the total votes?* Diana DeGette won the election with 272,892 votes or 73.8% of the total votes. 

## Election-Audit Summary: 
The Python script used in the audit was successful in providing the requested information and analysis for the Election Commission.  This script may also be useful in other election audits by changing just a few lines of code.  For example, the script calls and uses a specific csv file to access the election data.  For a new election audit, I would just have to update the location and name of the document containing the new data to analyze it using the same script.  I would also need to modify the code to save the audit results to a new document and location than the document used in this particular audit.  
