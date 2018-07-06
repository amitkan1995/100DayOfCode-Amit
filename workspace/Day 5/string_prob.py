# To check if string is made up of unique characters or not.

def unique(s):
    uniq_c=set() #Set are much faster as compared to list
    for c in s:
        if c in uniq_c:
            return False # If character exists in string then return false
        uniq_c.add(c)
    return True

st="garbzhiyfexaax" #Input string not unique
# st="uarbzhiyfexcwjp"  Unique input string
if unique(st):
    print("String is unique")
else:print("String is not unique")