# You will be give a set of poll data called election_data.csv.
# The dataset is composed of three columns: Voter ID, County, and Candidate.
# Your task is to create a Python script that analyzes the votes and calculates
# each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

filePath = os.path.join("Resources","election_data.csv")

with open(filePath,'r',encoding='utf-8',newline='') as csvFile:

	pollData = csv.DictReader(csvFile, delimiter=',')

# number of votes
	nVotes = 0

# Set of Candidate name who received votes
	CandidateName = set()

# New dictionary with Candidate name with number of received votes
	CandidateDict = {}
	
	for row in pollData:
		nVotes += 1
		tempCandidate = row["Candidate"]

		# if tempCandidate in CandidateDict.keys():
		# 	CandidateDict[tempCandidate] += 1
		# else:
		# 	CandidateDict[tempCandidate] = 1

		# Count number of vote for each Candidate using CandidateName set (old code)
		if tempCandidate not in CandidateName:
			CandidateName.add(tempCandidate)
			CandidateDict[tempCandidate] = 1
		else:
			CandidateDict[tempCandidate] += 1

	print("Election Results")
	print("-------------------------")
	print(f"Total Votes: {nVotes}")
	print("-------------------------")

# Print each Candidate with ratio of received votes and number of received votes.
	sorted(CandidateDict)
	for x in CandidateDict.keys():
	  	Ratio = round(CandidateDict[x] / nVotes * 100, 3)
	  	print(f"{x}: {Ratio}% ({CandidateDict[x]}) ")

# Find winner of Candidate using max function
	winner = max(CandidateDict, key=CandidateDict.get)

	print("-------------------------")
	print(f"Winner: {winner}")
	print("-------------------------")
