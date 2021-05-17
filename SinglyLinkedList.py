class node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class singleLinkedList:
    
    def __init__(self):
        self.head = None
       
    def insert_front(self, data):
        temp = node(data)
        if (self.head) != None:
            temp.link = self.head
            self.head = temp
        else:
            self.head = temp

    def display(self):
        if (self.head) == None:
            print("Empty")
            return
        else:
            disp = self.head
            while(disp != None):
                print(disp.data, end = ' ')
                disp = disp.link
        print('')

            
LL = singleLinkedList()
LL.insert_front(30)
LL.insert_front(20)
LL.insert_front(10)
LL.display()
