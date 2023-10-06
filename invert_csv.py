import csv


input_file = 'Tesi/out6.csv'


column1_index = 5  
column2_index = 8  

with open(input_file, 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    current_line=0
    for row in reader:
        current_line+=1
        if (row[5]=="ping"):

            
            data = []
            with open(input_file, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    data.append(row)

            for row in data:
                row[column1_index], row[column2_index] = row[column2_index], row[column1_index]


            with open(input_file, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(data)
            
            break    

