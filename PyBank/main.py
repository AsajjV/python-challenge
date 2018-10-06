import os
import csv
budget_csv = os.path.join("budget_data.csv")
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    num_months = len(list(csvreader))

print ("Financial Analysis")
print ("-------------------------")
print (f"Total Months:  {num_months}")
