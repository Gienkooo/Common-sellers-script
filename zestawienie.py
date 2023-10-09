import csv
import os

#nazwa pliku
filename = 'Zestawienie2022.csv'
#numer pola z kodem towaru
product_id = 2
#numer pola z kodem KTH
kth_id = 0
#twój kod KTH
kth = 'K007438'
#liczba linii w nagłówku
header_n = 2
#liczba linii w stopce
foot_n = 2

csvfile = open(filename, newline='')

i = 0
while os.path.exists(f"opracowanie {i} {filename}"):
    i += 1

csvoutput = open(f"opracowanie {i} {csvfile.name}", 'x')

reader = csv.reader(csvfile)
writer = csv.writer(csvoutput, dialect='excel', lineterminator='\n')

rows = []
for row in reader:
    if row[0] == '':
        break
    rows.append(row)

for row in rows[:header_n]:
    writer.writerow(row)

dict = {}
for row in rows[header_n:len(rows) - foot_n]:
    if row[product_id] in dict:
        dict[row[product_id]].add(row[kth_id])
    else:
        dict[row[product_id]] = {row[kth_id]}

filtered_set = set()
for key, val in dict.items():
    if (kth in val) and (len(val) > 1):
        filtered_set.add(key)

for row in rows[header_n:len(rows) - foot_n]:
    if row[product_id] in filtered_set:
        writer.writerow(row)
    
for row in rows[len(rows) - foot_n:]:
    writer.writerow(row)