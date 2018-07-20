# To store information in CSV file

#import necessery libraries
import csv

def detailsinput():
    details={}
    details['Name']=input("Enter name: ")
    details['Reg no']=int(input("Enter Registration No. : "))
    details['Physics']=int(input("Enter Physics marks: "))
    details['Chemistry']=int(input("Enter Chemistry marks: "))
    details['Maths']=int(input("Enter Maths marks: "))
    details['Percentage']=int(input("Enter Total Percentage: "))
    
    details['Course']=input("Enter course: ")
    details['Status']=input("Enter status of student: ")
    

    return  details

def writeToCsv(detail):
    with open('details.csv', 'w') as csvfile:
        fieldnames = ['Name','Reg no','Course','Physics','Chemistry','Maths','Percentage','Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(detail)
    print("Writing complete")
    
def readFromCsv():

    with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['Reg no'], row['Course'], row['Physics'], row['Maths'], row['Percentage'], row['Status'])


def editdetails():
    print("Enter Updated details:")
    deta=detailsinput()
    for row in reader:
        if name == row['name']:
            with open('details.csv', 'w') as csvfile:
                writer.writerow({'name': row['name'], 'number': row['number'], 'address': row['address']})
                writer.writerow(detail)
    print("Writing complete")





print("1. For New entry:")
print("2. Edit details of any student")
print("3. Display Details of Students")
print("4. Change Status of Student")
ch=int(input())
det={}
if ch==1:
    det=detailsinput()
    writeToCsv(det)
elif ch==2:
    
elif ch==3:
    readFromCsv()  
elif ch==4:

    
