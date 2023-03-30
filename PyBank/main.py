#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path


# In[2]:


csv_path = Path("budget_data.csv")
csv_data = pd.read_csv(csv_path)


# In[3]:


csv_data.shape


# In[4]:


total_months = csv_data.shape[0]


# In[5]:


csv_data.head()


# In[6]:


net_total = f"${csv_data['Profit/Losses'].sum()}"


# In[7]:


average_of_changes = csv_data['Profit/Losses'].mean()
average_of_changes = round(average_of_changes, 2)


# In[8]:


Profits = []
Losses = []
for number in csv_data['Profit/Losses']:
    if number > 0:
        Profits.append(number)
    elif number < 0:
        Losses.append(number)
greatest_profit_increase = max(Profits) - min(Profits)
highest_month = 0
greatest_loss_decrease = max(Losses) - min(Losses)
lowest_month = 0


# In[9]:


for index, row in csv_data.iterrows():
    if row['Profit/Losses'] == max(Profits):
        highest_month = row['Date']
    if row['Profit/Losses'] == min(Losses):
        lowest_month = row['Date']


# In[10]:


with open('financial_report.txt', 'w') as file:
    file.write(f"Financial Analysis")
    file.write('\n'+f"--------------------------")
    file.write('\n'f"Total Month: {total_months}")
    file.write('\n'f"Total: {net_total}")
    file.write('\n'f"Average Change: ${average_of_changes}")
    file.write('\n'f"Greatest Increase in Profits: {highest_month} (${greatest_profit_increase})")
    file.write('\n'f"Greatest Decrease in Profits: {lowest_month} (${greatest_loss_decrease})")
file.close()
    


# In[ ]:




