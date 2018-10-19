# Python 3 program to Check if lowercase and  
# uppercase characters are in same order 
  
# Function to check if both the  
# case follow the same order  
def isCheck(str) : 
  
    length = len(str) 
    lowerStr, upperStr = "", "" 
  
    # Traverse the string  
    for i in range(length) : 
  
        # Store both lowercase and  
        # uppercase in two different 
        # strings  
        if (ord(str[i]) >= 65 and 
            ord(str[i]) <= 91) : 
            upperStr = upperStr + str[i] 
  
        else : 
            lowerStr = lowerStr + str[i] 
  
    # transfor lowerStr to uppercase 
    transformStr = lowerStr.upper() 
  
    return transformStr == upperStr 
  
# Driver Code 
if __name__ == "__main__" : 
  
    str = "geeGkEEsKS"
      
    if isCheck(str) : 
        print("Yes") 
    else : 
        print("No") 