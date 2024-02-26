import csv

def write_csv(header,data,filename):
    with open(filename, 'w', newline="") as file: #open the csv file
         csvwriter = csv.writer(file) # 2. create a csvwriter object
         csvwriter.writerow(header) # 4. write the header
         csvwriter.writerows(data) # 5. write the rest of the data


# runs write_csv if it does not recive an input it will 
# run wite_csv with example values
def run_write_csv(header=[],data=[],filename=""):
    if not header:
            header = ['Name', 'Course1 Score', 'Course2 Score']
    if not data:
           data = [['Ali', 92, 80], ['Jonny', 75, 56], ['Mikey', 85, 98]]
    if not filename:
       filename="./studentscore.csv"
    write_csv(header,data,filename)

def read_csv(filename):
    data = []
    with open(filename, 'r') as fileobj:
         csvreader = csv.reader(fileobj)
         header = next(csvreader)
         for row in csvreader:
             data.append(row)
    return header,data


def run_read_csv(filename=""):
    if not filename:
       filename="./studentscore.csv"
    header,data=read_csv(filename)
    print(header,data)

run_write_csv()
run_read_csv()



