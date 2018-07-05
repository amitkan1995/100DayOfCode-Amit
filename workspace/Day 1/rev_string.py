#To reverse the string without using any string function
#Using Loop
st='hello there'

s=""
for i in st:
    s=i+s #Adding character to another string
    print(s)