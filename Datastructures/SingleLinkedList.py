class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None

   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.head is None:
         self.head = NewNode
         return
      laste = self.head
      while(laste.next):
         laste = laste.next
      laste.next=NewNode
# Print the linked list
   def listprint(self):
      printval = self.head
      while printval is not None:
         if not printval.next:
            print(printval.data, end = '')
         else :        
            print (printval.data, end = '->')
         printval = printval.next

def add(head1, head2):
    sol = SLinkedList()
    temp1, temp2 = head1, head2
    c = 0
    while temp1 and temp2:
        val = temp1.data + temp2.data + c
        d1 = val % 10
        c = val // 10
        sol.AtEnd(d1)
        temp1 = temp1.next
        temp2 = temp2.next

    while temp1:
       val = temp1.data + c
       d1 = val % 10
       c = val // 10
       sol.AtEnd(d1)
       temp1 = temp1.next
    
    while temp2:
       val = temp2.data + c
       d1 = val % 10
       c = val // 10
       sol.AtEnd(d1)
       temp2 = temp2.next

    ## reverse 
    temp3 = sol.head
    prev = None
    while(temp3):
        Next = temp3.next
        temp3.next = prev
        prev = temp3
        temp3 = Next
    sol.head = prev

    print()
    sol.listprint()



if __name__ == '__main__':
    l1 = SLinkedList()
    l2 = SLinkedList()

    for i in range(1,5):
        l1.AtEnd(i)
    
    for i in range(2,7):
        l2.AtEnd(i)
    
    l1.listprint(); print()
    l2.listprint(); print()
    temp1, temp2  = l1.head, l2.head
    prev1 = prev2 = None
    while(temp1): # reversing l1
        Next = temp1.next
        temp1.next = prev1
        prev1 = temp1
        temp1 = Next

    while(temp2): # reversing l1
        Next = temp2.next
        temp2.next = prev2
        prev2 = temp2
        temp2 = Next
    l1.head = prev1
    l2.head = prev2
    # adding logic
    add(l1.head, l2.head)
