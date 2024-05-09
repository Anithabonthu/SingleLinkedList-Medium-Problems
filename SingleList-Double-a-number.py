#!/usr/bin/env python
# coding: utf-8

# In[7]:


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
                print(temp.data)
                temp=temp.next
def doubleIt(head):
    num=0
    node=head
    while node:
        num=num*10+node.data
        node=node.next
    num=num*2
    if num==0:
        return Node(num)
    ptr=None
    while num:
        curr=Node(num%10)
        curr.next=ptr
        ptr=curr
        num=num//10
    return ptr
list1=LinkedList()
while True:
    print("1.Insertion  2.Traverse 3.exit" )
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        list1.insert(value)
    elif ch==2:            
        list1.print()
    elif ch==3:
        break
list1.head=doubleIt(list1.head)
list1.print()


# In[ ]:





# In[ ]:




