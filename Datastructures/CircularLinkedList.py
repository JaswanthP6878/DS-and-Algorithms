class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CSLL:
    def __init__(self):
        self.head= None
    
    def add_data(self, my_data): ## Adding only at the beginning
      New = Node(my_data)
      temp = self.head    
      New.next = self.head
      if self.head is not None:
         while(temp.next != self.head):
            temp = temp.next
         temp.next = New
      else:
         New.next = New
      self.head = New

    def delete(self, pos):
        if(pos > self.size()): print('\nPos not present'); return
        if (self.size() == 1): self.head = None; return
        if pos == 0:
            new_head = self.head.next
            temp = self.head.next
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_head
            self.head = new_head
        else :
            prev = None
            temp = self.head
            for i in range(pos):
                prev = temp
                temp = temp.next
            prev.next = temp.next

    def size(self):
        if self.head == None: return 0
        size = 1
        temp = self.head.next
        while temp != self.head:
            temp = temp.next
            size += 1
        return size

    def print_it(self):
        if(self.size() == 0) : print("Empty List "); return
        temp = self.head
        if self.head is not None:
            while(True):
                print("%d->" %(temp.data),end = ""),
                temp = temp.next
                if (temp == self.head):
                    break

if __name__ == '__main__':
    '''
        Example Question for CCSL.
    '''
    channels = CSLL()
    n = int(input())
    k = int(input())
    for i in range(n,0,-1):
        channels.add_data(i)
    index = k-1
    while(channels.size() > k-1):
        index= index % channels.size()
        channels.delete(index) 
        print()
        index = index + k - 1
    channels.print_it()
