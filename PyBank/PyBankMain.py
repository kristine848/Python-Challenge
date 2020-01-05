#import CSV
import csv
import os


#create path to file
csvpath = os.path.join("Resources","budget_data.csv")

#Open File and move to first line of data/skip headers
with open(csvpath) as csvfile:
    budgetfile=csv.reader(csvfile)
    next(budgetfile, None)
    
#Create dictionaries 
    Date= []
    PL= []
    Change= []

#assign dictionaries to existing rows in files
    for row in budgetfile:
        PL.append(float(row[1]))
        Date.append(row[0])

   #calcualte the average change and populate data into dictionary

    for i in range(1,len(PL)):
        Change.append(PL[i] - PL[i-1])   
        AvgChange = sum(Change)/len(Change)

#Find teh max change and min change from Change dictionary 
        Max = max(Change)

        Min = min(Change)

#Find what date the max an min chagne occured
        MaxLine = str(Date[Change.index(max(Change))])
        MinLine = str(Date[Change.index(min(Change))])
        
#print everything 
    print("Financial Analysis")
    print("Total Months:", len(Date))
    print("Total Revenue: $", sum(PL))
    print("Average Change: $", round(AvgChange))
    print("Greatest Increase in Profits:", MaxLine,"($", Max,")")
    print("Greatest Decrease in Profits:", MinLine,"($", Min,")")

