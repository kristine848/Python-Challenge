#import CSV and OS
import os
import csv

# Create dictionaries and variables
Candidates = []
TotalVotes = 0
VoteCounts = []


#Create CSVpath

CSVpath = os.path.join("Resources","election_data.csv")

 # Open current CSV and skip header row
with open(CSVpath) as csvFile:
    ElectionData = csv.reader(csvFile, delimiter=',')
    line = next(ElectionData,None)

# Count number of votes in list and designate column 2 for Candidates dictionary
    for line in ElectionData:
        TotalVotes = TotalVotes + 1
        CandidateList = line[2]

 # Create a liste of unique candiates and count the votes for each one by looping through with if statement
        if CandidateList in Candidates:
            UniqueCand = Candidates.index(CandidateList)
            VoteCounts[UniqueCand] = VoteCounts[UniqueCand] + 1
        else:
            Candidates.append(CandidateList)
            VoteCounts.append(1)

# Create variables to calculate % or votes and find the winner
    percentages = []
    MaxVotes = VoteCounts[0]
    MaxIndex = 0

# Loop through data the number times that equals the number of rows in file. COunt votes and divide by total to get percentage. Append to percentages dictionary
    for count in range(len(Candidates)):
        PercentOfVotes = VoteCounts[count]/TotalVotes*100
        percentages.append(PercentOfVotes)
#use if statment to detrimne winner by find which candiate has the highest number of votes
        if VoteCounts[count] > MaxVotes:
            MaxVotes = VoteCounts[count]
            print(MaxVotes)
            MaxIndex = count
    winner = Candidates[MaxIndex]

# Round percentages

    percentages = [round(i,3) for i in percentages]

# Print all data
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {TotalVotes}")
    for count in range(len(Candidates)):
        print(f"{Candidates[count]}: {percentages[count]}% ({VoteCounts[count]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")