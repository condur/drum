class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        '''method for setting the data field of the node'''
        self.data = data

    def getData(self):
        '''method for getting the data field of the node'''
        return self.data

    def setNext(self, next):
        '''method for setting the next field of the node'''
        self.next = next

    def getNext(self):
        '''method for getting the next field of the node'''
        return self.next

    def hasNext(self):
        '''returns true if the node points to another node'''
        return self.next is not None

    def insertAtBeginning(self, data):
        '''method for inserting a new node at the beginning of the Linked List
          (at the head)'''
        newNode = Node()
        newNode.setData(data)

        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
            self.length += 1

    def insertAtEnd(self, data):
        '''method for inserting a new node at the end of a Linked List'''
        newNode = Node()
        newNode.setData(data)

        current = self.head

        while current.hasNext():
            current = current.getNext()
            current.setNext(newNode)
            self.length += 1

    def deleteFromBeginning(self):
        '''method to delete the first node of the linked list'''
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1

    def clear(self):
        self.head = None
