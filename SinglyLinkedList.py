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
    #Deleting an element
    def delete_ele(self, ele):
        #Empty list, nothing to delete
        if(self.head) == None:
            print("List is Empty")
            return
        #If element to delete is first element
        if (self.head.data) == ele:
            trav = self.head
            self.head = trav.link
            trav = None
            return
        #Traverse list to find element
        trav = self.head
        flag = False
        while trav.link != None:
            #If element is found; delete
            if trav.link.data == ele:
                temp = trav.link;
                trav.link = temp.link
                temp = None
                flag = True
            if trav.link:
                trav = trav.link
        if flag == False:
            print("Element", ele, " not found!")            
    #Search an element
    def search_ele(self, ele):
        #Empty list, nothing to search
        if(self.head) == None:
            print("List is Empty")
            return
        trv = self.head
        spot = 0
        found = False
        while trv != None:
            if trv.data == ele:
                print(ele, "is present at position ", spot)
                found = True
            trv = trv.link
            spot += 1
        if found == False:
            print(ele, 'is not present in the list')

    #Displaying/printing all the elements of the list
    def display(self):
        if (self.head) == None:
            print("List is Empty")
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
LL.delete_ele(0)
LL.delete_ele(50)
LL.delete_ele(99)
LL.display()

LL.insert_pos(0,2)
LL.insert_pos(0,4)
LL.display()
LL.search_ele(0)
LL.search_ele(13)
