#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path
import csv

# Read in `menu_data.csv` and set its contents to a separate list object
menu_path = Path("menu_data.csv")
menu_data = pd.read_csv(menu_path)

#Initialize an empty `menu` list object to hold the contents of `menu_data.csv`
#Use a `with` statement and open the `menu_data.csv` by using its file path
#Use the `reader` function from the `csv` library to begin reading `menu_data.csv`
#Use the `next` function to skip the header (first row of the CSV)
menu = []
with open(menu_path, newline="") as file:
    csvreader = csv.reader(file, delimiter=",")
    csv_header = next(csvreader)

#Loop over the rest of the rows and append every row to the `menu` list object (the outcome will be a list of lists)
    for row in csvreader:
        menu.append(row)
file.close()
sales_path = Path("sales_data.csv")
sales_data = pd.read_csv(sales_path)

# Set up the same process to read in `sales_data.csv`. However, instead append every row of the sales data to a new `sales` list object.
sales = []
with open(sales_path, newline="") as file:
    csvreader = csv.reader(file, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        sales.append(row) 

# Initialize an empty `report` dictionary to hold the future aggregated per-product results
    report = {}

# Loop through every row in the `sales` list object, set Quantity and Menu_Item to their own variables
    for row in sales:
        quantity = row[3]
        menu_item = row[4]

# Perform a quick check if the `sales_item` is already included in the `report`. If not, initialize the key-value pairs for the particular `sales_item` in the report. Then, set the `sales_item` as a new key to the `report` dictionary and the values as a nested dictionary
        sales_item = menu_item    
        
        if sales_item not in report:
            report[sales_item] = {
                "01-count": 0,
                "02-revenue": 0,
                "03-cogs": 0,
                "04-profit": 0,
            }
            
# Create a nested loop by looping through every record in `menu`, set following columns to their own variables
        for row in menu:
            item = row[0]
            price = row[3]
            cost = row[4]

# Calculate profit
            if sales_item == item: 
                quantity = int(quantity)
                price = int(price)
                cost = int(cost)
                profit = quantity * price - cost
                
# Cummulatively add the values to corresponding metrics in report
                report[sales_item]["01-count"] += quantity
                report[sales_item]["02-revenue"] += price * quantity
                report[sales_item]["03-cogs"] += cost * quantity
                report[sales_item]["04-profit"] += profit * quantity
            else:
                print(f"{report[sales_item]} does not equal {item}! No Match!")
file.close()

# Write out the contents of the report and export it to a text file
with open('ramen_report.txt', 'w') as file:
    for item, item_maps in report.items():
        file.write(f"{item} {item_maps}\n")
        
file.close()


# In[ ]:




