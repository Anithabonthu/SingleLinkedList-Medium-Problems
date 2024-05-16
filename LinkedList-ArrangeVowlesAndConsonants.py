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
                print(temp.data)
                temp=temp.next
def arrangeCV(head):
        vowels=[]
        consonants=[]
        current=head
        while current:
            if current.data in "aeiou":
                vowels.append(current.data)
            else:
                consonants.append(current.data)
            current=current.next
            
        result=vowels+consonants
        ptr=None
        while result:
            curr=Node(result.pop())
            curr.next=ptr
            ptr=curr
        return ptr
list1=LinkedList()
while True:
    print("1.Insertion  2.Traverse 3.exit" )
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=input("Enter data value: ")
        list1.insert(value)
    elif ch==2:            
        list1.print()
    elif ch==3:
        break
list1.head=arrangeCV(list1.head)
list1.print()


# In[ ]:





# In[ ]:




