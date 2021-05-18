class node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert_front(self, data):
        #Create new node with data input
        newNode = node(data)
        
        #If list is empty, add new node as head
        if(self.head) == None:
            self.head = newNode
            return
        #Add new node to front of list
        else:
            #Point new node's next to head
            newNode.next = self.head
            #Point head's previous to new node
            self.head.prev = newNode
            #Make new node head node
            self.head = newNode
    
    def display(self):
        #If list is empty, nothing to print
        if self.head == None:
            print('List is empty!')
            return
        #Traverse list and print data
        else:
            trav = self.head
            while(trav != None):
                print(trav.data, end = ' ')
                trav = trav.next

DLL = DoublyLinkedList()
DLL.insert_front(30)
DLL.insert_front(20)
DLL.insert_front(10)
DLL.display()
