# Reverse a linked list

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
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("null")

    # method 1 -> iterative method
    # Time and space complexity: O(n) O(1)

    def reverseLinkedListIterative(self):
        currentHead = self.head
        previous = None
        tempNode = None
        while currentHead:
            tempNode = currentHead.next
            currentHead.next = previous
            previous = currentHead
            currentHead = tempNode
        self.head = previous
        print("After reverse:")
        self.printList()
        

    # method 2 -> Recursive Method:
    # Time Complexity: O(n) Auxiliary Space: O(1)

    
if __name__ == "__main__":
    llist = LinkedList()
    llist.appendAtHead(30)
    llist.appendAtHead(40)
    llist.appendAtHead(50)
    llist.appendAtHead(60)
    llist.appendAtHead(70)
    llist.appendAtHead(80)
    llist.appendAtHead(90)
    llist.printList()
    llist.reverseLinkedListIterative()
