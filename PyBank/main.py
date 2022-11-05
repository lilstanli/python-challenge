import os
import csv

os.system("cls")

# Assign the csv path to a variable
budgetDataPath = "Resources/budget_data.csv"

# Read csv file
with open(budgetDataPath, "r", encoding="utf8") as budgetData:
    budgetDataReading = csv.reader(budgetData, delimiter=",")
    budgetDataHeader = next(budgetDataReading)
    fullBudget = []
    monthlyValues = []
    monthsCount = 0
    netTotal = 0
    
    # Iterate through csv data and append both the full budget and only values' lines to variables
    for line in budgetDataReading:
        monthsCount += 1
        netTotal += int(line[1])
        fullBudget.append(line)
        monthlyValues.append(line[1])

# initialise and empty list to hold the monthly changes later
monthlyChanges = []

# iterate through only the monthly values and append the calculated changes to "MonthlyChanges" variable
for index, amount in enumerate(monthlyValues):
    if index < len(monthlyValues) and index - 1 >= 0:
        monthlyChanges.append(int(amount) - int(monthlyValues[index - 1]))

# Perform Average Change operation
averageChange = round(sum(monthlyChanges)/len(monthlyChanges), 2)

# Iterate through Monthly Changes and deduce the Greatest Increase and Greatest Decrease values
for index, singleChange in enumerate(monthlyChanges):
    if singleChange == max(monthlyChanges):
        greatestIncrease = fullBudget[index + 1]

    if singleChange == min(monthlyChanges):
        greatestDecrease = fullBudget[index + 1]

# Analysis of Budget
analysis = f'''
    Financial Analysis
    ----------------------------
    Total Months: {monthsCount}
    Total: ${netTotal}
    Average Change: ${averageChange}
    Greatest Increase in Profits: {greatestIncrease[0]} (${max(monthlyChanges)})
    Greatest Decrease in Profits: {greatestDecrease[0]} (${min(monthlyChanges)})
'''
print(analysis)

#export analysis to "analysis.txt" text file
analysisPath = "analysis/analysis.txt"
with open(analysisPath, "x") as analysisFile:
    analysisFile.write(analysis)
