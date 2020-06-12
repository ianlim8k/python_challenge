import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Open the csv file in read mode
with open(election_csv, 'r') as csvfile:

    # Split the data in file using commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row 
    header = next(csvreader)

    total_voters = 0
    candidate_list = []
    votes_won = []
    votes_won_percentage = []

    election_result = dict()
    counter = 0

    #read data from next row
    for row in csvreader:
        # Count the total number of votes
        total_voters += 1

        # Get the candidates list who receives votes
        candidates = row[2]
        if len(row[2]) == 0 or row[2] in candidate_list:
            pass
        else:
            candidate_list.append(row[2])

        #Get the vote count for each candidate
        if candidates in election_result:
            vote_count = election_result[candidates]
            vote_count += 1
            election_result[candidates] = vote_count           
        else:
        #Add candidate and vote count to result list in dictionary
            vote_count = 1
            election_result.update({candidates : vote_count})

    #calculate percentage won and determine winner

    for candidate_name in election_result:  
        #calculate the percentage won for each candidate
        percentage_won = (election_result[candidate_name] / total_voters) * 100
        #format the percentage to 3 decimal places and add % sign
        percentage_won = str(format(percentage_won,'.3f') + '%')
        #Add percentage won to list
        votes_won_percentage.append(percentage_won)
        
        #get the total votes won per candidate and add to list
        votes_total = election_result[candidate_name]
        votes_won.append(votes_total)       
        
        #Get the candidate with the most votes won
        if election_result[candidate_name] == max(election_result.values()):
            winner = candidate_name
        else:
            pass
      
    # zip the candidates, percentage won and votes won into a list/tuple
    final_result = zip(candidate_list,votes_won_percentage, votes_won)
   
    # Specify the file to write to
    output_path = os.path.join("Analysis", "Election_Results.txt")
    #open the file in write mode
    with open(output_path, 'w') as txtfile:

    # Write the first row (column headers)
        txtfile.write("Election Results\n")
        txtfile.write("----------------------\n")
        txtfile.write("Total Votes: %s\n" % (total_voters))
        txtfile.write("----------------------\n")
        for line in final_result:
            candidate_result = " ".join(str(i) for i in line)
            txtfile.write(" %s\n" % (candidate_result))
        txtfile.write("------------------\n")
        txtfile.write("Winner: %s\n" % (winner))
        txtfile.write("------------------\n")

    #print final result to terminal

    final_result = zip(candidate_list,votes_won_percentage, votes_won)
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {str(total_voters)}")
    print("--------------------------")
    #print candidates results from list
    for result in final_result:
        print(result[0], ":", result[1], "(", str(result[2]), ")")    
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")
   
        