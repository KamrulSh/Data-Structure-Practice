# Pairwise swap elements of a given linked list
# Move last element to front of a given Linked List

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

    def printList(self, head):
        current = head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("null")

    # Time and space complexity: O(n)
    def pairWiseSwapElement(self):
        print("--- After swap ---")
        current = self.head
        if current is None:
            return
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next
        self.printList(self.head)

    def moveLastElelentToHead(self):
        current = self.head
        while current and current.next:
            previous = current
            current = current.next
        previous.next = None
        current.next = self.head
        self.head = current
        print("--- After move last element ---")
        self.printList(self.head)
    

if __name__ == "__main__":
    llist = LinkedList()
    nlist = [40, 50, 60, 70, 80, 90]
    for i in range(len(nlist)):
        llist.appendAtHead(nlist[i])
        llist.printList(llist.head)
    llist.pairWiseSwapElement()
    print("-"*50)

    ll = LinkedList()
    sl = [ 'a', 'b', 'a', 'c', 'a', 'b', 'z' ]
    for i in range(len(sl)):
        ll.appendAtHead(sl[i])
        ll.printList(ll.head)
    ll.pairWiseSwapElement()
    ll.moveLastElelentToHead()
