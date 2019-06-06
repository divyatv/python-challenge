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

# Find the csv input file and load it on the csvfile variable.
csvfile= os.path.join('budget_data.csv')
print (csvfile)

# Open the file for reading.
with open(csvfile, 'r', newline='') as csvpybankfile:
    # read the file object into the variable using csv module.
    csvreader=csv.reader(csvpybankfile)
    #This will print the object.
    print(csvreader)
    #Skip the first header line inthe csv file.
    next(csvreader)
    #Set a counter to count the number of months.
    # ** Assuming that there are no repition of the months in the CSV file. **
    Total=0
    count =0
    #For every row in the csv file, print the line or do something else.
    for row in csvreader:
        # Printing the rows to see what I get.
        #print(row[0])
        count = count +1
        Total = int(row[1]) + Total
    





print ("-------------------------------------------------------------------")
print ("Total Months: ", count)
print ("Total: $",Total)
print ("Average  Change: $-2315.12")
print ("Greatest Increase in Profits: Feb-2012 ($1926159)")
print ("Greatest Decrease in Profits: Sep-2013 ($-2196167)")
print ("--------------------------------------------------------------------") 




