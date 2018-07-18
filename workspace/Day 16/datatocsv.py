# To store information in CSV file

#import necessery libraries
import csv

def detailsinput():
    details={}
    details['name']=input("Enter name: ")
       
    details['Reg no']=int(input("Enter Registration No. : "))

    marks={}
    marks['Physics']=int(input("Enter Physics marks: "))
    marks['Chemistry']=int(input("Enter Chemistry marks: "))
    marks['Maths']=int(input("Enter Maths marks: "))
    marks['Percentage']=int(input("Enter Total Percentage: "))
    details['Marks']=marks
    details['course']=input("Enter course: ")



with open('details.csv', 'w') as csvfile:
    fieldnames = []
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    
print("Writing complete")