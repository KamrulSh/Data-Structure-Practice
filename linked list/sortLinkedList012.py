# Sort a linked list of 0s, 1s and 2s

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

    def sortLinkedList012s(self):
        current = self.head
        count = [0]*3
        while current:
            count[current.data] += 1
            current = current.next
        index = 0
        current = self.head
        while current:
            if count[index] == 0:
                index += 1
            else:
                current.data = index
                count[index] -= 1
                current = current.next
        print("After sort:")
        self.printList()

              


if __name__ == "__main__":
    llist1 = LinkedList()
    nlist1 = [1, 1, 0, 2, 1, 0, 2]
    # nlist1 = [12,14,33]
    for i in range(len(nlist1)):
        llist1.appendAtHead(nlist1[i])
    llist1.printList()
    llist1.sortLinkedList012s()

