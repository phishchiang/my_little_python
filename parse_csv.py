import csv

'''
# Common way : Just use reader&writer 
with open('D:\\python\\pythonFun\\data\\csv\\crimeStolenCaseTaipei.csv', 'r', encoding='utf-8') as csv_file:
  csv_reader = csv.reader(csv_file)
  # To skip the first raw of data
  # next(csv_reader)
  with open('D:\\python\\pythonFun\\data\\csv\\new_crimeStolenCaseTaipei.csv', 'w', encoding='utf-8') as new_csv_file:
    csv_writer = csv.writer(new_csv_file, delimiter='\t')
    for line in csv_reader:
      # print (line)
      csv_writer.writerow(line)
'''

# Dictionary way 
with open('D:\\python\\pythonFun\\data\\csv\\crimeStolenCaseTaipei.csv', 'r', encoding='utf-8') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  # for line in csv_reader:
  #   print (line['發生(現)地點'])

  fieldnames = ['編號', '案類', '發生(現)日期', '發生時段']
  with open('D:\\python\\pythonFun\\data\\csv\\new_crimeStolenCaseTaipei.csv', 'w', encoding='utf-8') as new_csv_file:
    csv_writer = csv.DictWriter(new_csv_file, fieldnames = fieldnames, delimiter='\t')
    # If you want the fieldnames in the first row
    csv_writer.writeheader()
    for line in csv_reader:
      # print (line)
      del line['發生(現)地點']
      csv_writer.writerow(line)
