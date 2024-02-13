# Place code below to do the analysis part of the assignment.
import csv
import os

analyze = {}
with open(os.path.join("data", 'cleaned_data.csv'), 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if len(row[13]) > 0:
            analyze[row[0]] = row[13]

avg = 0
year = 1880
index = 0
for k, v in analyze.items():
    if index < 10:
        avg += float(v)
        index += 1
    else:
        avg = avg / 10
        print(f"{year} to {year + 9}: {avg:.2f}")
        year += 10
        avg = float(v)
        index = 1

                    
