# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter, candidate options and votes, declare dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #Print each row in the csv file
    for row in file_reader:
       #2. Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # 2. Add a vote to that candidates count
        candidate_votes[candidate_name] +=1   
#Determine the percentage of votes for each candidate by looping though the counts
# 1. Iterate through the candidate list
for candidate_name in candidate_votes:
    #2.retrieve vote count of a candidate
    votes = candidate_votes[candidate_name] 
    #3. calculate the percentage of votes
    vote_percentage = float(votes)/float(total_votes)*100
    #4. print the candidate name and percentage of votes
    
    #to do - print out each candidates name, vote cout, and percentage of the 
    #votes to the terminal

    #determine winning vote count and candidate
    #Determine if the vcotes is great than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning _percentage=vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # and set the winning candidate = to candidates name
        winning_candidate = candidate_name
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#to do print out winning candidate, vote count and $ to terminal
#print (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

   