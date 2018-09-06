# Reverse Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    # Funtion to add new node at the begining
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    #To print linked list
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

llist = LinkedList()
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
llist.reverse()

print("reverse Linked List is ")
llist.printList()