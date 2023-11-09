import csv
from datetime import datetime
from os import write

with open("Tesi/out6.csv", 'r') as file:
    current_line = 0
    csv_reader = csv.reader(file)
    for _ in csv_reader:
        current_line += 1

total_lines = current_line
host4 = (total_lines-1) //4 + 1
host5 = ((total_lines-1) // 4) * 2 +1
host6 = ((total_lines-1) // 4) * 3 +1
host7 = ((total_lines-1) // 4) * 4 +1


with open("Tesi/out6.csv", 'r') as file:
    csv_reader=csv.reader(file)
    current_line=0
    data_ip_4="0"
    data_ip_5="0"
    data_ip_6="0"
    data_ip_7="0"

    for row in csv_reader:
        current_line+=1
        if(row[5]=="ping"): 
            break
        if current_line==host4:
            if len(row) >= 5:
                data_ip_4=row[5]
                print(data_ip_4, "\n")
        elif current_line==host5:
            if len(row) >= 5:
                data_ip_5=row[5]
                print(data_ip_5, "\n")
        elif current_line==host6:
            if len(row) >= 5:
                data_ip_6=row[5]
                print(data_ip_6, "\n")
        elif current_line==host7:
            if len(row) >= 5:
                data_ip_7=row[5]
                print(data_ip_7)

result=0
data_4=float(data_ip_4)
data_5=float(data_ip_5)
data_6=float(data_ip_6)
data_7=float(data_ip_7)
if data_4<=data_5 and data_4<=data_6 and data_4<=data_7:
    result=1
elif data_5<data_4 and data_5<=data_6 and data_5<=data_7:
    result=2
elif data_6<data_4 and data_6<data_5 and data_6<=data_7:
    result=3
elif data_7<data_4 and data_7<data_5 and data_7<data_6:
    result=4
else:
    result=1

with open("Tesi/result.txt", 'w') as file1:
    file1.write(str(result))

