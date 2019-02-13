import os
import csv

budget_data_csv = os.path.join('./', 'budget_data.csv')

total_month = []
total_change = []
monthly_change = []

with open(budget_data_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)

    for row in csv_reader:
        total_month.append(row[0])
        total_change.append(int(row[1]))

    for i in range(len(total_change) - 1):
        monthly_change.append(total_change[i + 1] - total_change[i])

    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Month: {len(total_month)}')
    print(f'Total: ${sum(total_change)}')
    print(f'Average Change: ${sum(monthly_change) / len(monthly_change):.2f}')
    print(f'Greatest Increase in Profits: '
          f'{total_month[monthly_change.index(max(monthly_change)) + 1]} (${max(monthly_change)})')
    print(f'Greatest Decrease in Profits: '
          f'{total_month[monthly_change.index(min(monthly_change)) + 1]} (${min(monthly_change)})')

csv_file.close()

