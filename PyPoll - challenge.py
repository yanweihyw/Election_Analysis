# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
county_options=[]
# Declare the empty dictionary.
candidate_votes = {}
county_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county = ""
winning_countycount = 0
winning_countypercentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
# Print each row in the CSV file.
    for row in file_reader:
# 2. Add to the total vote count.
        total_votes += 1
# Print the candidate name from each row.
        candidate_name = row[2]
        county_name=row[1]
# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
# Add it to the list of candidates.
           candidate_options.append(candidate_name)
#Begin tracking that candidate's vote count. 
           candidate_votes[candidate_name] = 0
       
# Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#county calculation
# If the county does not match any existing county...
        if county_name not in county_options:
# Add it to the list of counties.
           county_options.append(county_name)
#Begin tracking that county's vote count. 
           county_votes[county_name] = 0
# Add a vote to that county's count
        county_votes[county_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate in candidate_votes:
# 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
# 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

# Determine the percentage of votes for each county by looping through the counts.
# 1. Iterate through the county list.
    for county in county_votes:
# 2. Retrieve vote count of a county.
        countyvotes = county_votes[county]
# 3. Calculate the percentage of votes.
        countyvote_percentage = int(countyvotes) / int(total_votes) * 100
# Determine winning vote count and candidate
# Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
# If true then set winning_count = votes and winning_percent =
# vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
# And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

#winning county
# Determine winning vote county count and county
# Determine if the votes is greater than the winning county count.
        if (countyvotes > winning_countycount) and (countyvote_percentage > winning_countypercentage):
# If true then set winning_count = votes and winning_percent =
# vote_percentage.
            winning_countycount = countyvotes
            winning_countypercentage = countyvote_percentage
# And, set the winning_candidate equal to the candidate's name.
            winning_county = county


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
# Save the final vote count to the text file.
    txt_file.write(election_results)

#county
# Save the final vote count to the text file.
    print("County Votes:\n") 
    for county in county_votes:
        # Retrieve vote count and percentage.
        countyvotes = county_votes[county]
        countyvote_percentage = float(countyvotes) / float(total_votes) * 100
        county_results = (
            f"{county}: {countyvote_percentage:.1f}% ({countyvotes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning county.
        if (countyvotes > winning_countycount) and (countyvote_percentage > winning_countypercentage):
            winning_countycount = countyvotes
            winning_county = county
            winning_countypercentage = countyvote_percentage
    # Print the winning county's results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"

        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)


    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    # Save the results to our text file.


