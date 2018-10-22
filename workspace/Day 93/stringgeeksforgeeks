#include <cstring> 
#include <iostream> 
using namespace std; 
  
bool isInGivenBase(string str, int base) 
{ 
    // Allowed bases are till 16 (Hexadecimal) 
    if (base > 16) 
    return false; 
  
    // If base is below or equal to 10, then all 
    // digits should be from 0 to 9. 
    else if (base <= 10)  
    { 
    for (int i = 0; i < str.length(); i++) 
        if (!(str[i] >= '0' and 
             str[i] < ('0' + base))) 
            return false; 
    } 
  
    // If base is below or equal to 16, then all 
    // digits should be from 0 to 9 or from 'A'  
    else
    { 
    for (int i = 0; i < str.length(); i++) 
        if (! ((str[i] >= '0' && 
                str[i] < ('0' + base)) ||                                  
                (str[i] >= 'A' && 
                 str[i] < ('A' + base - 10)) 
            ))                  
            return false; 
    } 
    return true;  
} 
  
// Driver code 
int main() 
{ 
    string str = "AF87"; 
    if (isInGivenBase(str, 16)) 
    cout << "Yes"; 
    else
    cout << "No"; 
    return 0; 
} 