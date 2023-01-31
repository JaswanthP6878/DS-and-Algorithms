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
            prev = temp
            temp = temp.next
        sol = temp.data
        if prev:
            prev.next = None
        else :
            self.head = None
        self.top -= 1
        return sol
    
    def peek(self):
        if not self.head: print('Stack is Empty'); return
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp.data
        
    def prints(self):
        if not self.head : print('empty stack'); return
        temp = self.head
        while temp:
            print(temp.data, end = '->')
            temp = temp.next


def fun(a,b):
    a.push(b.pop())


if __name__ == '__main__':
    s1=Stack()
    s2=Stack()
    s3=Stack()
    s1.push(30)
    s1.push(20)
    s1.push(10)
    fun(s3,s1)
    fun(s2,s1)
    fun(s2,s3)
    fun(s3,s1)
    fun(s1,s2)
    fun(s3,s2)
    fun(s3,s1)
    s3.prints()