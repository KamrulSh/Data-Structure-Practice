# Sort a linked list of 0s, 1s and 2s

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

    def mergeTwoLinkedList(self, list1, list2):
        dummyNode = Node(-1)
        endNode = dummyNode
        list1 = list1.head
        list2 = list2.head
        while True:
            if list1 is None:
                endNode.next = list2
                break
            if list2 is None:
                endNode.next = list1
                break
            if list1.data <= list2.data:
                endNode.next = list1
                list1 = list1.next
            else:
                endNode.next = list2
                list2 = list2.next
            endNode = endNode.next
        self.head = dummyNode.next
        print("After merge:")
        self.printList()

        # after reverse
        previous = None
        newHead = dummyNode.next
        tempNode = None

        while newHead:
            tempNode = newHead.next
            newHead.next = previous
            previous = newHead
            newHead = tempNode
        self.head = previous
        print("After reverse:")
        self.printList()
              


if __name__ == "__main__":
    llist1 = LinkedList()
    nlist1 = [11, 13, 20, 25, 31, 40, 42]
    # nlist1 = [22,23,24]
    for i in range(len(nlist1)):
        llist1.appendAtTail(nlist1[i])
    llist1.printList()

    llist2 = LinkedList()
    nlist2 = [1, 11, 30, 32, 51, 60, 72]
    # nlist2 = [12,13,14]
    for i in range(len(nlist2)):
        llist2.appendAtTail(nlist2[i])
    llist2.printList()

    llist1.mergeTwoLinkedList(llist1, llist2)
 

