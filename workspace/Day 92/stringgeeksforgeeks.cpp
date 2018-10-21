
// C++ implementation of above approach 
#include <bits/stdc++.h> 
using namespace std; 
  
// function to calculate minimum 
// characters to replace 
int replace(string A, string B) 
{ 
  
    int n = A.length(), m = B.length(); 
    int count = 0, i, j; 
  
    for (i = 0; i < n; i++) { 
        for (j = 0; j < m; j++) { 
  
            // mismatch occurs 
            if (A[i + j] != B[j])  
                break; 
        } 
  
        // if all characters matched, i.e, 
        // there is a substring of 'a' which 
        // is same as string 'b' 
        if (j == m) { 
            count++; 
  
             // increment i to index m-1 such that 
            // minimum characters are replaced 
            // in 'a' 
            i += m - 1; 
             
        } 
    } 
  
    return count; 
} 
  
// Driver Code 
int main() 
{ 
    string str1 = "aaaaaaaa"; 
    string str2 = "aaa"; 
  
    cout << replace(str1 , str2); 
  
  return 0; 
} 
