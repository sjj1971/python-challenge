
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


#import csv
import csv
with open('budget_data.csv', 'r') as csv_file:
	csvReader = csv.DictReader(csv_file)

	totalDate = 0
	totalAmount = 0
	totalChange = 0
	previousAmount = 0
	maxIncrease = 0
	maxDecrease = 0
	
	for row in csvReader:
		tempDate = row['Date']
		tempAmount = int(row['Profit/Losses'])

# calculate total number of months
		totalDate += 1
# calculate net total amount of "Profit/Losses"
		totalAmount += tempAmount

# calculate amount of changes in "Profit/Losses" from second row
		if totalDate > 1:
			tempChange = tempAmount - previousAmount
			totalChange += tempChange
			previousAmount = tempAmount		

#calculate greatest increase and greatest decrease in profits
			if maxIncrease < tempChange:
				maxIncrease = tempChange
				maxIncreaseDate = tempDate
			elif maxDecrease > tempChange:
				maxDecrease = tempChange
				maxDecreaseDate = tempDate
			else: continue
		elif totalDate == 1:
			previousAmount = tempAmount
		else: continue

averageChange = totalChange / (totalDate-1)

print('Financial Analysis')
print('----------------------------')
print('Total Months: {}'.format(totalDate))
print('Total: ${}'.format(str(totalAmount)))
print('Average  Change: ${}'.format(str(round(averageChange,2))))
print('Greatest Increase in Profits: {} (${})'.format(maxIncreaseDate, str(maxIncrease)))
print('Greatest Decrease in Profits: {} (${})'.format(maxDecreaseDate, str(maxDecrease)))
