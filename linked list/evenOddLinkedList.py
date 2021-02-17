# Segregate even and odd nodes in a Linked List

# split the linked list into two: 
# one containing all even nodes and 
# other containing all odd nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def appendAtTail(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def printList(self):
        print("List:")
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("null")

    def separateEvenAndOdd(self):
        if self.head is None:
            return
        evenHead = evenTail = None
        oddHead = oddTail = None
        current = self.head
        while current:
            if current.data % 2 == 0:
                if evenHead is None:
                    evenHead = current
                    evenTail = evenHead
                else:
                    evenTail.next = current
                    evenTail = evenTail.next
            else:
                if oddHead is None:
                    oddHead = current
                    oddTail = oddHead
                else:
                    oddTail.next = current
                    oddTail = oddTail.next
            current = current.next

        if evenHead is None or oddHead is None:
            return self.head
        oddTail.next = None
        evenTail.next = oddHead
        self.head = evenHead
        print("Even odd:")
        self.printList()
              


if __name__ == "__main__":
    llist1 = LinkedList()
    nlist1 = [11, 13, 20, 25, 31, 40, 42]
    # nlist1 = [22,24,26]
    for i in range(len(nlist1)):
        llist1.appendAtTail(nlist1[i])
    llist1.printList()
    llist1.separateEvenAndOdd()

    llist2 = LinkedList()
    nlist2 = [1, 11, 30, 32, 51, 60, 72]
    # nlist2 = [12,13,14]
    for i in range(len(nlist2)):
        llist2.appendAtTail(nlist2[i])
    llist2.printList()
    llist2.separateEvenAndOdd()
 

