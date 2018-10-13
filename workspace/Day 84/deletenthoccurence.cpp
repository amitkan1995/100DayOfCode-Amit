
// A C++ program to demonstrate deletion of last 
// Node in singly linked list 
#include <bits/stdc++.h> 
  
// A linked list Node 
struct Node { 
    int key; 
    struct Node* next; 
}; 
  
void deleteLast(Node* head, int key) 
{ 
    // Initialize previous of Node to be deleted 
    Node* x = NULL; 
  
    // Start from head and find the Node to be 
    // deleted 
    Node* temp = head; 
    while (temp) { 
        // If we found the key, update xv 
        if (temp->key == key) 
            x = temp; 
  
        temp = temp->next; 
    } 
  
    // key occurs at-least once 
    if (x != NULL) { 
  
        // Copy key of next Node to x 
        x->key = x->next->key; 
  
        // Store and unlink next 
        temp = x->next; 
        x->next = x->next->next; 
  
        // Free memory for next 
        delete temp; 
    } 
} 
  
/* Utility function to create a new node with 
   given key */
Node* newNode(int key) 
{ 
    Node* temp = new Node; 
    temp->key = key; 
    temp->next = NULL; 
    return temp; 
} 
  
// This function prints contents of linked list 
// starting from the given Node 
void printList(struct Node* node) 
{ 
    while (node != NULL) { 
        printf(" %d ", node->key); 
        node = node->next; 
    } 
} 
  
/* Drier program to test above functions*/
int main() 
{ 
    /* Start with the empty list */
    struct Node* head = newNode(1); 
    head->next = newNode(2); 
    head->next->next = newNode(3); 
    head->next->next->next = newNode(5); 
    head->next->next->next->next = newNode(2); 
    head->next->next->next->next->next = newNode(10); 
  
    puts("Created Linked List: "); 
    printList(head); 
    deleteLast(head, 2); 
    puts("\nLinked List after Deletion of 1: "); 
    printList(head); 
    return 0; 
} 
