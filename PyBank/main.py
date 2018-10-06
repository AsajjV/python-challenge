import os
import csv
budget_csv = os.path.join("budget_data.csv")

date = []
amount = []
change_in_amount = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader) 

    for row in csvreader:
        date.append(row[0])
        amount.append(int(row[1]))
        
    for i in range(1,len(amount)):
        change_in_amount.append(amount[i] - amount[i-1])   
        avg_change = sum(change_in_amount)/len(change_in_amount)

        greatestprofit=max(change_in_amount)
        month_greatest_profit = str(date[change_in_amount.index(greatestprofit)])

        greatestloss=min(change_in_amount)
        month_greatest_loss = str(date[change_in_amount.index(greatestloss)])

totalmonths = len(date)
totalprofitloss = sum(amount)

#print(profit)
#print(losses)
#print (date)
#print(change_in_amount)        
#print(totalmonths)
#print(totalprofitloss)
#print(greatestprofit)
#print(change_in_amount)
#print (round(avg_change, 2))
#print(greatestloss)
#print(month_greatest_profit)
#print(month_greatest_loss)
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofitloss}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {month_greatest_profit} ${greatestprofit}")
print(f"Greatest Decrease in Losses: {month_greatest_loss} ${greatestloss}")
