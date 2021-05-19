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
   
   def insert_end(self, data):
        #Create new node with input data
        newNode = node(data)

        #If list is empty, add new node as head
        if (self.head) == node:
            self.head = newNode
            return

        else:
            trav = self.head
            #Traverse to the end of the list and add new node
            while (trav.next) != None:
                trav = trav.next
            #Point last node's next to new node
            trav.next = newNode
            #Point new node's previous to old last node
            newNode.prev = trav

        def insert_after(self, ele, data):
        #If list is empty, print error and add node as new
        if self.head == None:
            print("List is empty! A new list is created with", data)
            insert_front(data)
            return
        else:
            #Create new node
            flag = False
            newNode = node(data)
            trav = self.head
            #Traverse the list
            while (trav) != None:
                #If the element is found to insert after
                if trav.data == ele:
                    #Insert new node after element
                    newNode.next = trav.next
                    newNode.prev = trav
                    trav.next = newNode
                    flag = True
                    return
                trav = trav.next
            #If element not found and insertion not made, print error
            if flag == False:
                print(ele, "not found in list!")

        def del_node(self, ele):
        #list is empty, print error
        if self.head == None:
            print("List is empty!")
            return
        #We travese the list and check cases for deletion
        else:
            trav = self.head
            while (trav) != None:
                if trav.data == ele:
                    #1 There is only one element in list, and will be deleted
                    if trav.next == None and trav.prev == None:
                        #Make the single node none
                        trav = None
                        head = None
                        return
                    #2 If the first element is to be deleted
                    elif trav.next != None and trav.prev == None:
                        #Move head to next element
                        self.head = self.head.next
                        #Make new head previous none
                        self.head.prev = None
                        trav = None
                        return
                    #3 If element is in between
                    elif trav.next != None and trav.prev != None:
                        #Pointing the previous node of trav to node next to trav
                        trav.prev.next = trav.next
                        #Pointing the next node of trav to node behind trav
                        trav.next.prev = trav.prev
                        trav = None
                        return
                    #4 Last element to be deleted
                    else:
                        trav.prev.next = None
                        trav = None
                        return
                trav = trav.next
            print(ele, "not found!")


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
DLL.insert_end(40)
DLL.insert_after(10, 15)
DLL.insert_after(40, 45)
DLL.insert_after(50, 55)
DLL.display()
DLL.del_node(10)
DLL.display()
DLL.del_node(15)
DLL.del_node(45)
DLL.del_node(30)
DLL.del_node(55)
DLL.display()
