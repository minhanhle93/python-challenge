#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path

# Read the CSV file into Pandas dataframe
csv_path = Path("budget_data.csv")
csv_data = pd.read_csv(csv_path)

# Calculate the total number of months
csv_data.shape
total_months = csv_data.shape[0]

# Calculate the net total amount of Profit/Losses
net_total = f"${csv_data['Profit/Losses'].sum()}"

# Calculate the average of changes in Profit/Losses
csv_data["change"] = csv_data['Profit/Losses'].diff()
average_of_changes = csv_data["change"].mean()

# Calculate the greatest increase in profits (date and amount)
# First, Profits is isolated into a list, then, the difference between the lowest and highest Profit is calculated
# The same is done with Losses
Profits = []
Losses = []
for number in csv_data['Profit/Losses']:
    if number > 0:
        Profits.append(number)
    elif number < 0:
        Losses.append(number)
greatest_profit_increase = max(Profits) - min(Profits)
greatest_loss_decrease = max(Losses) - min(Losses)

# Date of highest Profit and greatest Loss
highest_month = 0
lowest_month = 0
for index, row in csv_data.iterrows():
    if row['Profit/Losses'] == max(Profits):
        highest_month = row['Date']
    if row['Profit/Losses'] == min(Losses):
        lowest_month = row['Date']
        
# Print out the analysis result and export to a text file
with open('financial_report.txt', 'w') as file:
    file.write(f"Financial Analysis")
    file.write('\n'f"--------------------------")
    file.write('\n'f"Total Month: {total_months}")
    file.write('\n'f"Total: {net_total}")
    file.write('\n'f"Average Change: ${average_of_changes}")
    file.write('\n'f"Greatest Increase in Profits: {highest_month} (${greatest_profit_increase})")
    file.write('\n'f"Greatest Decrease in Profits: {lowest_month} (${greatest_loss_decrease})")
file.close()

