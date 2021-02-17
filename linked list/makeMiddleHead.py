# Function to make middle element as head

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

    def makeMiddleElementHead(self):
        current = self.head
        if current is None or current.next is None:
            return current
        # find middle element
        count = 0
        while current:
            count += 1
            current = current.next
        middle = int(count/2)
        midElement = self.head
        previous = None
        for i in range(middle):
            previous = midElement
            midElement = midElement.next
        previous.next = previous.next.next
        midElement.next = self.head
        self.head = midElement
        print("Mid is head:")
        self.printList()
        return midElement        


if __name__ == "__main__":
    llist1 = LinkedList()
    # nlist1 = [90, 80, 70, 60, 50, 30, 20]
    nlist1 = [12,14,33]
    for i in range(len(nlist1)):
        llist1.appendAtHead(nlist1[i])
    llist1.printList()
    llist1.makeMiddleElementHead()
