#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new
    def print(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
def OddEvenList(head):
    if not head or not head.next:
        return head
    odd=head
    even=head.next
    ehead=even
    while even and even.next:
        odd.next=even.next
        odd=even.next
        even.next=odd.next
        even=odd.next
    odd.next=ehead
    return head
list1=LinkedList()
print("Enter Elements into List.")
while True:
    print("1.Insertion  2.Traverse  3.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        list1.insert(value)
    elif ch==2:            
        list1.print()
    elif ch==3:
        break
list1.head=OddEvenList(list1.head)
list1.print()


# In[ ]:





# In[ ]:




