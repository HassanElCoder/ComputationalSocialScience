import csv

def write_csv(header,data,filename):
    with open(filename, 'w', newline="") as file: #open the csv file
         csvwriter = csv.writer(file) # 2. create a csvwriter object
         csvwriter.writerow(header) # 4. write the header
         csvwriter.writerows(data) # 5. write the rest of the data


header = ['Name', 'Course1 Score', 'Course2 Score']
data = [['Ali', 92, 80], ['Jonny', 75, 56], ['Mikey', 85, 98]]
filename="./studentscore.csv"
write_csv(header,data,filename)


