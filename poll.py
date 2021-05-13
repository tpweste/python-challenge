import os
import csv

csvpath = os.path.join('election_data.csv')

count = 0
candidate = []
percentage = []
candidate_vote = {}
total = 0
average = 0

  

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)


    for row in csvreader:
        count += 1
        candidate=row[2]
        
        # counts all the votes for each candidate
        if candidate in candidate_vote.keys():
            candidate_vote[candidate] += 1
        else:
            candidate_vote[candidate]=1
    
    # calculates and prints the result for each candidate as percentage and total votes per each 

  
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {count}")
    print("----------------------------")
   
    for total in candidate_vote:
        
        percentage = (candidate_vote[total]/count)*100
        
        print(f"{total} {round(percentage,2)}% {candidate_vote[total]}")   

    # printing the winner
    print("----------------------------")
    print(f"Winner:", max(candidate_vote, key=lambda key: candidate_vote[key]))
    print("----------------------------")
    
  
output_file = os.path.join('election_results.csv')

with open(output_file, "w") as datafile:   
    datafile.write("Election Results\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total votes: {count}\n")
    datafile.write("----------------------------\n")
    
    for total in candidate_vote:
        percentage = (candidate_vote[total]/count)*100
        datafile.write(f"{total} {round(percentage,2)}% {candidate_vote[total]}\n")
        
    datafile.write("----------------------------\n")
    datafile.write(f"Winner:{ max(candidate_vote, key=lambda key: candidate_vote[key])}\n")
    datafile.write("----------------------------\n")
    