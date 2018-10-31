
// C++ implementation of the approach 
#include <bits/stdc++.h> 
using namespace std; 
  
// Function that removes the 
// characters which have even 
// frequencies in the string 
void solve(string s) 
{ 
    // create a map to store the 
    // frequency of each character 
    unordered_map<char, int> m; 
    for (int i = 0; i < s.length(); i++) { 
        m[s[i]]++; 
    } 
  
    // to store the new string 
    string new_string = ""; 
  
    // remove the characters which 
    // have even frequencies 
    for (int i = 0; i < s.length(); i++) { 
  
        // if the character has 
        // even frequency then skip 
        if (m[s[i]] % 2 == 0) 
            continue; 
  
        // else concatenate the 
        // character to the new string 
        new_string += s[i]; 
    } 
  
    // display the modified string 
    cout << new_string << endl; 
} 
  
// Driver code 
int main() 
{ 
    string s = "aabbbddeeecc"; 
  
    // remove the characters which 
    // have even frequencies 
    solve(s); 
  
    return 0; 
} 
