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
    Candidates_Raw=[]
    CandidateCount=0
    for row in csvreader:
        Candidates_Raw.append(row[2])
    #print("Candidate list=", Candidates)

   

def findunique(list):
    uniquelist=[]
    for x in list:
        if x not in uniquelist:
            uniquelist.append(x)
            
    #for x in uniquelist:
    print("unique candidates are=:", uniquelist)  
    return uniquelist

UniqueList=findunique(Candidates_Raw)
print("Unique list of candidate=", UniqueList)
 

def Calculate_Winner(str, list2):
    numberofvotes=0
    TotalVotes=0
    PrintResult=[]
    NumHolder=[]
    for ele in list2:
        if (str==ele):
            numberofvotes=numberofvotes+1
        if str in list2:
            TotalVotes=TotalVotes+1    
     #print("Number of votes for ", eachcandidate,":", numberofvotes)
     #print(" Total Votes=", TotalVotes)
        percentage=(numberofvotes/TotalVotes)*100
        #print ( eachcandidate, "%=",percentage)
        NumHolder=[TotalVotes, numberofvotes, percentage]
        PrintResult=[str, NumHolder]
    return PrintResult;
     #### Writing the std out into a file and then printing the file content to terminal.
    

    #PrintResult=[eachcandidate, numberofvotes, TotalVotes, percentage]
    ##Return everything that you calculated
    #return[numberofvotes, TotalVotes, percentage];

newlist=[]    
for eachCandidate in UniqueList:
   #print("everyCandidate=", everyCandidate)
   #findpercent("everyCandidate", Candidates) 
 #list=Calculate_Winner(eachCandidate, Candidates_Raw) 
 list1=Calculate_Winner(eachCandidate, Candidates_Raw)
 newlist.append(list1)
 print("calculated list=", newlist)
#Calcualte_Winner("Correy", Candidates)
#Calcualte_Winner("Li", Candidates)
#Calcualte_Winner("O'Tooley", Candidates)         


### Writing the std out into a file and then printing the file content to terminal.
writefile=open('PyPoll_results.txt', 'w')
## Open a file and start writing terminal/stdout into the file
sys_out=sys.stdout
sys.stdout=writefile
##Print to the terminal part of the doe goes here:
print("-----------------------VIVEK-------------------------------")
print("Election Results")
print ("-----------------------------------------------------------")
print("Total Votes:", newlist[0][1][0])
print("--------------------------")
votes=[]
for i in range(len(newlist)):
  print(newlist[i][0], ":", round((newlist[i][1][2]), 4), "%", "(", newlist[i][1][1], ")")
  votes.append(newlist[i][1][1])   
maxvote=max(votes)
indexOfMaxVote=votes.index(maxvote)
print("---------------------------")
print ("Winner: ", newlist[indexOfMaxVote][0])
print("---------------------------")
#print("Winner: Khan")
print("---------------------------")
writefile.close()
sys.stdout=sys_out 







##Write from file to terminal.
pathoffile=os.path.join('PyPoll_results.txt')
print(pathoffile)
with open (pathoffile, 'r', newline='') as terminalprint:
    printtoterminal=terminalprint.read()
    print(printtoterminal)