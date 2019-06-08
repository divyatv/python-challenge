#Divya TV - Python homework - Calculating polling information.
# From the dat set provided- Calculate:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

## ***** Assuming that there is no frauds that is - same voter dindt cast vote
## ***** More than once in same of different county.

## Import os and csv to read from the files and write to files.
import os
import csv
import sys

## load the file and read csv file.
csvfile=os.path.join('PyPoll', 'election_data.csv')
print("path of the file=", csvfile)

with open(csvfile, 'r', newline='') as datafile:
    csvreader=csv.reader(datafile)
    print("csv data object=", csvreader)
    ## skip the header of the file.
    next(csvreader)

## Calculations reside here:
    #Initialising lists for calculations
    Candidates=[]
    CandidateCount=0
    for row in csvreader:
        Candidates.append(row[2])
    #print(Candidates)
def findunique(list):
    uniquelist=[]
    for x in list:
        if x not in uniquelist:
            uniquelist.append(x)
    for x in uniquelist:
        print("unique candidates are=:", x)   

findunique(Candidates)    

def findpercent(list):
    numberofvotes=[]
    for x in list:
        



#### Writing the std out into a file and then printing the file content to terminal.
writefile=open('PyPoll_results.txt', 'w')
## Open a file and start writing terminal/stdout into the file
sys_out=sys.stdout
sys.stdout=writefile
##Print to the terminal part of the doe goes here:
print("-----------------------VIVEK-------------------------------")
print("Election Results")
print ("-----------------------------------------------------------")
print("Total Votes: 3521001")
print("--------------------------")
print("Khan: 63.000% (2218231)")
print("Correy: 20.000% (704200)")
print("Li: 14.000% (492940)")
print("O'Tooley: 3.000% (105630)")
print("---------------------------")
print("Winner: Khan")
print("---------------------------")
writefile.close()
sys.stdout=sys_out

##Write from file to terminal.
pathoffile=os.path.join('PyPoll_results.txt')
print(pathoffile)
with open (pathoffile, 'r', newline='') as terminalprint:
    printtoterminal=terminalprint.read()
    print(printtoterminal)