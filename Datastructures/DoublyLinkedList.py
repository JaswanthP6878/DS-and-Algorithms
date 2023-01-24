class Node:
    def __init__(self, value):
        self.lnext = None
        self.rnext = None
        self.data = value

class DLL :
    def __init__(self):
        self.Head = None
    
    def insert(self,value, pos):
        New = Node(value)
        if self.Head == None:
            self.Head = New
        else :
            if pos > 0 and pos <= self.count()+1:
                if pos == 1:
                    New.rnext = self.Head
                    self.Head.lnext = New
                    self.Head = New
                else :
                    temp = self.Head
                    for i in range(0, pos-2):
                        temp = temp.rnext
                    New.rnext = temp.rnext
                    if temp.rnext:
                        temp.rnext.lnext = New
                    New.lnext = temp
                    temp.rnext = New

    def Display(self):
        temp = self.Head
        while temp != None:
            print(temp.data, end = " ")
            temp = temp.rnext

    def Delete(self, pos):
        if self.Head == None : print('list empty'); return
        if pos == 1:
            temp = self.Head
            self.Head = temp.rnext
        else :
            if pos > 0 and pos <= self.count() + 1:
                temp = self.Head
                for i in range(pos-1):
                    temp = temp.rnext
                ## middle element
                temp.lnext.rnext = temp.rnext
                if(temp.rnext): ##last case
                    temp.rnext.lnext = temp.lnext
            else :
                print('index out of range')
                

    def count(self):
        temp = self.Head
        cnt = 0
        while temp != None:
            cnt += 1
            temp = temp.rnext
        return cnt;

if __name__ == '__main__':
    ob = DLL()
    for i in range(1,5):
        ob.insert(i,1)
    ob.Display()
    ob.insert(2,3)
    print()
    ob.Display()
    ## delete test
    print()
    ob.Delete(10)
    ob.Display()