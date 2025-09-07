import csv
list_nums = []
with open('codeforces/13.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    list_nums.append(int(lines[0]))

print(sum(list_nums))