# singly linked list implementation using head
# some linked list operation

class ListNode:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def appendAtHead(self, new_value):
        newNode = ListNode(new_value)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        print(f"{new_value} added at head")

    def appendAtTail(self, new_value):
        newNode = ListNode(new_value)
        self.size += 1
        print(f"{new_value} added at tail")
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    # Search an element in the List by given value
    # method 1 --> iterative
    def searchElementByKeyIterative(self, key):
        current = self.head
        while current:
            if current.value == key:
                print(f"Element {key} Found (Iterative)")
                return True
            current = current.next
        print(f"Element {key} Not Found (Iterative)")
        return False

    # method 2 --> recursive
    def searchElementByKeyRecursive(self, current, key):
        if current is None:
            print(f"Element {key} Not Found (Recursive)")
            return False
        if current.value == key:
            print(f"Element {key} Found (Recursive)")
            return True
        return self.searchElementByKeyRecursive(current.next, key)

    # get Nth node in the List if it exists
    # method 1 --> iterative
    def getNthNodeIterative(self, position):
        current = self.head
        count = 0
        while current:
            if count == position:
                print(f"{position} th node is {current.value} (Iterative)")
                return current.value
            count += 1
            current = current.next
        
        print(f"{position} th position exceeded (Iterative)")
        return False

    # method 2 --> recursive
    def getNthNodeRecursive(self, current, position):
        count = 0
        if current:
            if count == position:
                print(f"n th node is {current.value} (Recursive)")
                return
            self.getNthNodeRecursive(current.next, position-1)

        else:
            print(f"n th position exceeded (Recursive)")

    # get the nth node from the last of a linked list
    # last node counts from 1
    def getNthNodeFromLast(self, position):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        current = self.head
        if position < count:
            for i in range(count-position):
                current = current.next
            print(f"{position} th from last is {current.value}")
        else:
            print(f"{position} th from last is exceeded")

    # Find the middle of a given linked list
    def findMiddleElement(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"Middle element is {slow.value}")
        return slow.value

    # counts the number of occurence of given element in the List
    # method 1 --> iterative
    def occurenceOfElementIterative(self, key):
        current = self.head
        count = 0
        while current:
            if current.value == key:
                count += 1
            current = current.next
        print(f"Element {key} occurs {count} times (iterative)")
        return count

    # method 2 --> recursive
    def occurenceOfElementRecursive(self, current, key):
        if current is None:
            print(f"Element {key} occurs 0 times (recursive)")
            return
        if current.value == key:
            return 1 + self.occurenceOfElementRecursive(current.next, key)
        self.occurenceOfElementRecursive(current.next, key)
    
    # Inserts a new node after the given prev_node
    def insertElementAfter(self, prev_node, new_value):
        current = self.head
        newNode = ListNode(new_value)
        # find the previous node
        while current:
            if current.value == prev_node:
                newNode.next = current.next
                current.next = newNode
                self.size += 1
                print(f"inserted {new_value} after {prev_node}")
                return
            current = current.next

        print(f"not found {prev_node} in the list to insert")
        
        
    # deletes the node if it is found same as provided key
    def deleteNodeByKey(self, key):
        current = self.head
        # if head is the key then it deletes
        if current is not None and current.value == key:
            self.head = current.next
            current = None
            self.size -= 1
            return
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change 'previous.next'
        while current is not None:
            if current.value == key:
                break
            previous = current
            current = current.next
        # if key is not present in linked list 
        if current == None:
            print(f"Element {key} not found")
            return
        # unlink the node from linked list 
        previous.next = current.next
        current = None
        print(f"Element {key} is deleted")
        self.size -= 1

    # delete the node at a given position
    def deleteNodeAtPosition(self, position):
        if self.head is None:
            return
        current = self.head
        # If head needs to be removed
        if position == 0:
            self.head = current.next
            current = None
            self.size -= 1
            print(f"Head deleted at position {position}")
            return 
        # Find previous node of the node to be deleted
        for i in range(position-1):
            current = current.next
            # If position is more than number of nodes
            if current.next is None:
                print(f"Exceed position {position}")
                return 
        
        newNext = current.next.next
        current.next = None
        current.next = newNext
        self.size -= 1
        print(f"Deleted {position}th position")

    # delete whole list by deleting each value
    def deleteLinkedList(self):
        # self.head = None
        current = self.head
        while current:
            previous = current.next
            del current.value
            current = previous
        self.size = 0
        print("All list deleted")

    # count items and print list
    def countAndPrintList(self):
        current = self.head
        count = 0
        print("-- List element --")
        while current:
            print(current.value)
            count += 1
            current = current.next
        print(f"-- Total items: {count} --\n")

if __name__ == '__main__':
    newList = LinkedList()
    newList.appendAtHead(20)
    newList.appendAtTail(40)
    newList.appendAtTail(30)
    newList.appendAtTail(30)
    newList.appendAtHead(90)
    newList.countAndPrintList()
    newList.insertElementAfter(55,77)
    newList.appendAtHead(55)
    newList.appendAtHead(66)
    newList.appendAtTail(33)
    newList.countAndPrintList()
    newList.insertElementAfter(33,77)
    newList.countAndPrintList()
    newList.getNthNodeIterative(7)
    newList.getNthNodeRecursive(newList.head, 1)
    newList.getNthNodeFromLast(8)
    newList.findMiddleElement()
    newList.deleteNodeByKey(30)
    newList.countAndPrintList()
    newList.deleteNodeAtPosition(6)
    newList.appendAtTail(30)
    newList.countAndPrintList()
    newList.searchElementByKeyIterative(77)
    newList.searchElementByKeyRecursive(newList.head, 78)
    newList.occurenceOfElementIterative(30)
    # newList.occurenceOfElementRecursive(newList.head, 30)
    # newList.deleteLinkedList()
    print("Size of list:", newList.size)