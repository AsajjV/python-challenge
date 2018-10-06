import os
import csv
budget_csv = os.path.join("budget_data.csv")

date = []
profit = []
losses = []
amount = []
change_in_amount = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)
    print (csvheader) 

    for row in csvreader:
        date.append(row[0])
        amount.append(int(row[1]))
        if int(row[1]) > 0:
            profit.append(int(row[1]))
        else: losses.append(int(row[1]))
        
    for i in range(1,len(amount)):
        change_in_amount.append(amount[i] - amount[i-1])   
        avg_change = sum(change_in_amount)/len(change_in_amount)

totalmonths = len(date)
totalprofitloss = sum(amount)
greatestprofit = max(profit)
#print(profit)
#print(losses)
#print (date)
#print(change_in_amount)        
#print(totalmonths)
#print(totalprofitloss)
#print(greatestprofit)
#print(change_in_amount)
print (round(avg_change, 2))