import os
import csv
election_csv = os.path.join("election_data.csv")

voterid = []
candidates = []

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)
    #print(csvheader)

    for row in csvreader:
        #voterid.append(row[0])
        #totalvotes=(len(voterid))

        #print(totalvotes)
        candidates.append(row[2])
        candidates_set = set(candidates)

print(candidates_set)
        

