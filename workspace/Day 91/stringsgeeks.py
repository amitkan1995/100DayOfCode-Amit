# Python 3 program to minimize the length of string  
# by removing occurrence of only one character 
  
# Function to find the minimum length 
def minimumLength(s) : 
  
    maxOcc = 0
    n = len(s) 
    arr = [0]*26
  
    # Count the frequency of each alphabet  
    for i in range(n) : 
        arr[ord(s[i]) -ord('a')] += 1
  
    # Find the alphabets with maximum frequency 
    for i in range(26) : 
        if arr[i] > maxOcc : 
            maxOcc = arr[i] 
  
    # Subtract the frequency of character  
    # from length of string  
    return n - maxOcc 
  
  
# Driver Code 
if __name__ == "__main__" : 
  
    str = "afddewqd"
    print(minimumLength(str)) 
  