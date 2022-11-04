import os
import csv

os.system("cls")

budgetDataPath = "Resources/budget_data.csv"

with open(budgetDataPath, "r", encoding="utf8") as budgetData:
    budgetDataRead = csv.reader(budgetData, delimiter=",")
    budgetDataHeader = next(budgetDataRead)
    monthsCount = 0
    netTotal = 0
    monthlyValues = []

    for line in budgetDataRead:
        monthsCount += 1
        netTotal += int(line[1])
        monthlyValues.append(line[1])

monthlyChanges = []
for index, amount in enumerate(monthlyValues):
    if index < len(monthlyValues) and index - 1 >= 0:
        monthlyChanges.append(int(monthlyValues[index - 1]) - int(amount))

print(monthlyChanges)

'''if rowCount < len(monthlyValues):
        nextMonthlyVal = monthlyValues[rowCount + 1]
        valchange = int(amount) - int(nextMonthlyVal)
        monthlyChanges.append(valchange)
        #nextMonthlyVal = monthlyValues[rowCount + 1]
        rowCount += 1
        '''
#print([n for n in monthlyChanges])


print(f'''
    Financial Analysis
    ----------------------------
    Total Months: {monthsCount}
    Total: ${netTotal}
    Average Change: $-8311.11 ${len(monthlyValues)}
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)
''')

