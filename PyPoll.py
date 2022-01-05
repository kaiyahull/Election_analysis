# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total volume counter
total_votes = 0

# Declare a new list for candidate names
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Declare vairable for the willing candidate (string)
winning_candidate = ""

# Declare a variable for the winning count equal to 0 
winning_count = 0

# Declare a variable for the winning percengage equal to 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read and analyze data here
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add the total vote count
        total_votes += 1

        # Gather candidate names from each row
        candidate_name = row[2]

        # If candidate name does not match a candidate already in the list
        if candidate_name not in candidate_options:
            #Add candidate name to the list of candidate options 
            candidate_options.append(candidate_name)
        
        #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Using the open() function with the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file:

    # Print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #Save the final vote count to the text file
    txt_file.write(election_results)

        # Iterate thorugh the candidate list
    for candidate_name in candidate_votes:
         # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

         #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f} %: ({votes:,})\n")
         
        # Print each candidate's name, vote count, and percentage
        print(candidate_results)

        # Save the candidate results to our text file
        txt_file.write(candidate_results)    

         # Determine the winning vote, percentage, and candidate
         # Determine the # of votes for each candidate is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If so, set the winning_count, winning_percentage, and winning_candidate 
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        # print(f"{candidate_name}: {vote_percentage:.1f} %: ({votes:,})\n")
            
        
    winning_candidate_summary = (
         f"--------------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"---------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
    
