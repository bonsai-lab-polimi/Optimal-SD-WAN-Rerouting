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

with open ("Tesi/times.txt", 'a') as file4:
    file4.write("new iteration:\n ip 10.0.0.4: ")
    file4.write(data_ip_4)
    file4.write("\n ip 10.0.0.5: ")
    file4.write(data_ip_5)
    file4.write("\n ip 10.0.0.6: ")
    file4.write(data_ip_6)
    file4.write("\n ip 10.0.0.7: ")
    file4.write(data_ip_7)
    file4.write("\nChosen path= ")
    file4.write(str(result))
    file4.write("\n\n\n")


with open("Tesi/result.txt", 'w') as file1:
    file1.write(str(result))

with open("Tesi/host.txt", 'a')  as file2:
    current_time= datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file2.write("Time: ")
    file2.write(str(current_time))
    file2.write("\n")
    if (data_ip_4=="0"):
        file2.write("File formatted incorrectly\n")
    elif result==1 or result==2:
        file2.write("Host 10.0.0.1\n")
    else:
        file2.write("Host 10.0.0.2\n")    
