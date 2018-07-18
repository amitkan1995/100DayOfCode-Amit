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
    
#def readFromCsc():



print("1. For New entry:")
print("2. Edit details of any student")
print("3. Display Details of Students")
ch=int(input())
det={}
if ch==1:
    det=detailsinput()
    writeToCsv(det)
