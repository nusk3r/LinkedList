class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class circularSingle:
    
    def __init__(self):
        self.head = None
    
    def insert_start(self, data):
        newNode = node(data)
        #Head is empty, add new node as head
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        #Traverse to the end of list
        trav = self.head
        while trav.next is not self.head:
            trav = trav.next
        #Point new node to head
        newNode.next = self.head
        #Update head 
        self.head = newNode
        #Point last element to new head
        trav.next = self.head
        
    def insert_end(self, data):
        #Create a new node
        newNode = node(data)
        #When list is empty, add node as new head
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        #Travese to the end of list
        trav = self.head
        while trav.next is not self.head:
            trav = trav.next
        #Point the last node to new node
        trav.next = newNode
        #Point the new node to head
        newNode.next = self.head
    
    def insert_after(self, ele, data):
        #Create a new node
        newNode = node(data)
        #In case list is empty
        if self.head is None:
            print('List is empty!')
            return
        #Traverse to the element
        trav = self.head
        while trav.next is not self.head:
            if trav.data is ele:
                #Point new node to next of current node
                newNode.next = trav.next
                #Point current node to new node 
                trav.next = newNode
                return
            trav = trav.next
            
        #Last element is not checked in the previous loop
        if trav.data is ele:
            #Point new node to next of current node
                newNode.next = trav.next
                #Point current node to new node 
                trav.next = newNode
                return  
        #element provided is not present in the list, print error
        print('Element not found!')
        
    def  del_node(self, ele):
        #When list is empty, print error
        if self.head is None:
            print('List is empty!')
            return
        #Element to delete is in head node
        if self.head.data is ele:
            #Traverse to last node and update pointer to head
            trav = self.head
            while trav.next is not self.head:
                trav = trav.next
            #Move pointer of last node to new head
            trav.next = self.head.next
            #Update head by moving to next node
            self.head = self.head.next

        #Traverse to the node before to be deleted
        trav = self.head
        while trav.next is not self.head:
            if trav.next.data is ele:
                trav.next = trav.next.next
                return
            trav = trav.next
        print('Element not found!')       
         
        
         
    
    #Displaying/printing all the elements of the list
    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        trav = self.head
        while (trav.next is not self.head):
            print (trav.data, end = ' ')
            trav = trav.next
        print (trav.data, end = ' ')
        print('')
        
CSL = circularSingle()
CSL.insert_start(20)
CSL.insert_start(10)
CSL.insert_end(30)
CSL.insert_after(20, 25)
CSL.insert_after(30, 40)
CSL.insert_after(50, 55)
CSL.display()
CSL.del_node(25)
CSL.del_node(10)
CSL.del_node(40)
CSL.del_node(45)
CSL.display()
        
