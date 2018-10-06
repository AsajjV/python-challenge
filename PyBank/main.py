import os
import csv
budget_csv = os.path.join("budget_data.csv")
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvfile)
    print (csvheader) 
    
    #Date=csvheader.index("Date")
    #ProfitLosses=csvheader.index("Profit/Losses")

    sum_profit = 0
    sum_loss = 0
    amount = 0

    for row in csvreader:
        amount = float(row[1])
        if float(amount) > 0:
            sum_profit = float(sum_profit) + float(amount)
        else:
            sum_loss = float(sum_loss) + float(amount)
    
    totalProfLoss=sum_loss + sum_profit
    num_months = len(list(csv.reader(open('budget_data.csv'))))-1


print ("Financial Analysis")
print ("-------------------------")
print (f"Total Months:  {num_months}")
print (f"Total:  ${totalProfLoss}")
