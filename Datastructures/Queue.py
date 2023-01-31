class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.tail = None
        self.max = 100
        self.ll = 0
    
    def isFull(self):
        return self.ll > self.max

    def enqueue(self, data):
        if (self.isFull == True): print('queue full!'); return

        New = Node(data)
        if not self.front:
            self.front = New
            self.tail = New
            return
        else :
            self.tail.next = New
            self.tail = New

    def dequeue(self):
        if not self.front:
            print('queue is empty'); return

        self.front = self.front.next


    def prints(self):
        temp = self.front
        while temp:
            print(temp.data, end = '->')
            temp = temp.next
        return


if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)

    q.dequeue()
    q.dequeue()

    q.prints()