import os
import csv
csvpath = os.path.join("budget_data.csv")
financial_analysis = os.path.join("financial_analysis.csv")

month = 'Date'
profits = 'Profit/Losses'
month_total = 0
total = 0
total_change = 0
max_increase = 0
max_decrease = 0
previous_row = 0


with open(csvpath, 'r', encoding='utf8') as csvfile:
    csv_reader = csv.DictReader(csvfile)


    for row in csv_reader:
      month_total += 1
      active_row = int(row[profits])
      active_month = row[month]
      total += active_row
      current_change = active_row - previous_row
      total_change += current_change if month_total != 1 else 0
      
      
      if current_change > max_increase:
        max_increase = current_change
        max_increase_month = active_month
        
      elif current_change < max_decrease:
        max_decrease = current_change
        max_decrease_month = active_month
      previous_row = active_row
    
output =  f'Financial Analysis\n'\
          f'------------------------\n'\
          f'Total Months: {month_total}\n'\
          f'Total: ${total}\n'\
          f'Average Change: ${total_change/(month_total - 1):.2f}\n'\
          f'Greatest Increase in Profits: {max_increase_month} (${max_increase})\n'\
          f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n'\

print(output)
#export data to text file int analysis folder - specify file to write  

with open(financial_analysis, 'w', encoding='utf8') as textfile:
    textfile.write(output)






