# Python assignment - pyBank - Divya TV
# 1- The total number of months included in the dataset
# 2- The net total amount of "Profit/Losses" over the entire period
# 3-  The average of the changes in "Profit/Losses" over the entire period
# 4-  The greatest increase in profits (date and amount) over the entire period
# 5- The greatest decrease in losses (date and amount) over the entire period
# 6- As an example, your analysis should look similar to the one below:
# Financial Analysis
#  -------------------------------------------------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
#---------------------------------------------------------------------
# Import modules for os and csv - to access their functions.
import os
import csv
import sys

# Find the csv input file and load it on the csvfile variable.
csvfile= os.path.join('PyBank','budget_data.csv')
print (csvfile)

# Open the file for reading.
with open(csvfile, 'r', newline='') as csvpybankfile:
    # read the file object into the variable using csv module.
    csvreader=csv.reader(csvpybankfile)
    #This will print the object.
    #print(csvreader)
    #Skip the first header line inthe csv file.
    next(csvreader)
    #Set a counter to count the number of months.
    # ** Assuming that there are no repition of the months in the CSV file. **
    Total=0
    count =0
    AverageChange=[]
    #For every row in the csv file, print the line or do something else.
        
    for row in csvreader:
        # Printing the rows to see what I get.

        #print(row)
        count = count +1
        Total = int(row[1]) + Total
        AverageChange.append(int(row[1]))
    #print(AverageChange)    
#print("length of first list which has total=", len(AverageChange))
print("-------------------------------------------------------------------")
##Creating a new list to hold the diffrences in profit and losses
newlist=[]
lengthrows=len(AverageChange)-1
#print("length of the newlist==", lengthrows)

##Loop through the old list, len.newlist times and append the differences
for i in range(lengthrows):
    newlist.append(AverageChange[i+1]-AverageChange[i])
#print("new list with averages =", newlist)

#Add everything in the list
total=sum(newlist, 0)
## Calculate the average
AverageChangenum=round((total/len(newlist)), 1)
#print("change in average=",AverageChangenum )

#Calculate the max and min in the new list.
GreatestIncrease=max(newlist)
#print("GreatestIncrease=", GreatestIncrease)

GreatestDecrease=min(newlist)
#print("GreatestDecrease=", GreatestDecrease)

## Print the results to a file.
writefile=open('pyBankResults.txt', 'w')
#writefile.write("Financial Analysis")
#writefile.close()
sys_out = sys.stdout
sys.stdout = writefile

 ## Printing results - writing whatever to the file.
print("Financial Analysis")
print ("-------------------------------------------------------------------")
print ("Total Months: ", count)
print ("Total: $",Total)
print ("Average  Change: $", AverageChangenum)
print ("Greatest Increase in Profits: Feb-2012 ($", GreatestIncrease, ")")
print ("Greatest Decrease in Profits: Sep-2013 ($", GreatestDecrease, ")")
print ("--------------------------------------------------------------------") 
writefile.close()
sys.stdout = sys_out


##Print the file to the terminal.
newfile=os.path.join('pyBankResults.txt')
with open(newfile, 'r', newline='') as terminaloutput:
    printterminal=terminaloutput.read()
    print(printterminal)
    

 






