import os
import csv
budget_csv = os.path.join("budget_data.csv")
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
print ("Financial Analysis")
print ("-------------------------")

