class node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class singleLinkedList:
    
    def __init__(self):
        self.head = None
    
    #Inserting an element at the front of the list
    def insert_front(self, data):
        newNode = node(data)
        #Create new node and point it to head, change head to point to new node
        if (self.head) != None:
            newNode.link = self.head
            self.head = newNode
        #The list is empty, add the new node to head
        else:
            self.head = newNode
    
    #Inserting an element at the end of the list
    def insert_end(self, data):
        newNode = node(data)
        #The list is empty, add the new node to head
        if (self.head) == None:
            self.head = newNode
        #Traverse to the end of list, then add new node
        else:
            tail = self.head
            while(tail.link):
                tail = tail.link
            tail.link = newNode
    
    #Insert at position p in the linked list
    def insert_pos(self, data, pos):
        #Position is negative, abort insertion
        if pos < 0:
            print('Invalid position!')
            return
        #If position is first, insert at front
        elif pos == 0:
            self.insert_front(data)
            return
        #Create new node with input data
        newNode = node(data)
        #List is empty, add new node as head
        if (self.head) == node:
            self.head = newNode
        #Traverse to posistion and insert new node
        else:
            count = 0
            trav = self.head
            #Traverse list until position is reached 
            while(count < pos - 1):
                if (trav.link != None):
                    trav = trav.link
                    count += 1
                else:
                    #Abort traverse if end of list is reached
                    break
            #Insert element if position is valid
            if count == pos - 1:
                newNode.link = trav.link
                trav.link = newNode
            else:
                #Position is out of range 
                print('Invalid position!')
                
    
    #Displaying/printing all the elements of the list
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
LL.insert_end(40)
LL.insert_end(50)
LL.display()
LL.insert_pos(0,3)
LL.insert_pos(0,9)
LL.insert_pos(0,0)
LL.display()
