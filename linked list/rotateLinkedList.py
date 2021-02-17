# Function to rotate LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def appendAtHead(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        print("List:")
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("null")

    # Method-1:
    def rotateLinkedList(self, k):
        current = self.head
        if k == 0:
            return None
        count = 0
        while current.next:
            count += 1
            if count == k and current.next:
                makeEnd = current
            current = current.next
            endNode = current
        # list length is less than k
        if k > count:
            print("Exceed")
            return 
        
        endNode.next = self.head
        self.head = makeEnd.next
        makeEnd.next = None
        print("After rotation of:", k)
        self.printList()

    # Method-2: making circular list
    def rotateLinkedListCircular(self, k):
        current = self.head
        if k == 0:
            return None
        count = 1
        while current.next:
            count += 1
            current = current.next
        # list length is less than k
        if k >= count:
            print("Exceed")
            return
        
        current.next = self.head
        newCurrent = self.head
        for i in range(1, k):
            newCurrent = newCurrent.next
        self.head = newCurrent.next
        newCurrent.next = None
        print("After rotation of:", k)
        self.printList()
              


if __name__ == "__main__":
    llist1 = LinkedList()
    nlist1 = [90, 80, 70, 60, 50, 30, 20]
    # nlist1 = [12,14,33]
    for i in range(len(nlist1)):
        llist1.appendAtHead(nlist1[i])
    llist1.printList()
    llist1.rotateLinkedList(6)
    llist1.rotateLinkedListCircular(5)
