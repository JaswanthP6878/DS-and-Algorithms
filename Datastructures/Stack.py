class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.top=-1
        self.max=100
    
    def push(self, value):
        if(self.isFull()) : print('stack full'); return 
        
        if self.head == None:
            self.head = Node(value)
        else :
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)
        self.top += 1
    
    def isFull(self):
        return not self.top < self.max

    def pop(self):
        prev = None
        temp = self.head
        while temp.next:
            temp = temp.next
        
        
    
    def prints(self):
        temp = self.head
        while temp:
            print(temp.data, end = '->')
            temp = temp.next


if __name__ == '__main__':
    s1 = Stack()
    for i in range(1,200):
        s1.push(i)
    s1.prints()