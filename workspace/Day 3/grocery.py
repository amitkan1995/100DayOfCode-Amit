#Get grocery information from text file
#  
import json

def tojson(gl):
    txt=json.dumps(gl)
    f=open("grocerylist.json","w")
    f.write(txt)
    f.close()

def readList(i_name):
    j_data=json.load(open('grocerylist.json'))
    print(j_data[i_name])


n=int(input("Enter the number of items (Input 0 if list is already there) : "))
grolist={}
#Adding items to dictionary
if n!=0:
    for i in range(n):
        item_name=input("Enter item name: ")
        item_quant=int(input("Enter quantity: "))
        grolist[item_name]=item_quant
    tojson(grolist)




searchQuery=input("Enter item to search: ")
readList(searchQuery)