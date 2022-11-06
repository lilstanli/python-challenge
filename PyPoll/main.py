# Author: Stanley Nyarko Aboagye
# Unit 3 Homework: Python 
# PyPoll

import os
import csv

os.system("cls")

# Assign the csv path to a variable
#electionDataPath = "../../Instructions/PyPoll/Resources/election_data.csv"
electionDataPath = "Resources/election_data.csv"

electionDataList = []
totalVotes = 0

# Read csv file
with open(electionDataPath, "r", encoding="utf8") as electionData:
    readingElectionData = csv.reader(electionData, delimiter=",")
    electionDataHeader = next(readingElectionData)
    
    # Iterate through csv data and append all lines to variable
    for line in readingElectionData:
        totalVotes += 1
        electionDataList.append(line)

# Grab Voting List by only Candidate Names
votesByCandidateName = [v[2] for v in electionDataList]

# Initialise empty list to subsequently hold only names of all candidates
candidateList = []
[candidateList.append(li) for li in votesByCandidateName if li not in candidateList]

# Append Candidate's name, Winning percentage and Vote count to List for use later
candidateSummary = []
[candidateSummary.append([c, round((((votesByCandidateName.count(c)) / totalVotes) * 100), 3), votesByCandidateName.count(c)]) for c in candidateList]

# Compute Winner of Election
def winner():
    groupedCount = []
    [groupedCount.append(c[2]) for c in candidateSummary]
    MaxCount = [i[0] for i in candidateSummary if max(groupedCount) == i[2]]
    return MaxCount[0]

# Capture the Candidate's name, Winning percentage and Vote count to a variable for use in the Final analysis
summary = ""
for t in range(len(candidateList)):
    summary += f"    {candidateSummary[t][0]}: {candidateSummary[t][1]}% ({candidateSummary[t][2]})\n"

# Final Analysis of Elections
analysis = f'''
    Election Results
    -------------------------
    Total Votes: {totalVotes}
    -------------------------
{summary}    -------------------------
    Winner: {winner()}
    -------------------------'''
print(analysis)


# Export analysis to "analysis.txt" text file
analysisPath = "analysis/analysis.txt"
with open(analysisPath, "x") as analysisFile:
    analysisFile.write(analysis)
