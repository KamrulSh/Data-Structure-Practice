# Python3 program to remove all elements
# provided by key in the linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def afterPrintList(self, newHead):
        # just for print start
        temp = newHead
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
        # just for print end

    # method 1 -> iterative
    def removeElementByKeyIterative(self, key):
        if self.head is None:
            return
        while self.head and self.head.data == key:
            self.head = self.head.next
        current = self.head
        while current and current.next:
            if current.next.data == key:
                current.next = current.next.next
            else:
                current = current.next
        print("Remove Element By Key Iterative =>")
        self.printList()
        return self.head

    # method 2 -> using dummy node
    def removeElementByKeyDummyNode(self, head, key):
        demoNode = Node(-1)
        demoNode.next = self.head
        currentNode = demoNode
        while currentNode and currentNode.next:
            if currentNode.next.data == key:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        # just for print start
        print("Remove Element By Key DummyNode =>")
        self.afterPrintList(demoNode.next)
        # just for print end
        return demoNode.next

    # Remove duplicates from a sorted linked list
    def removeDuplicatesSorted(self):
        current = self.head
        if current is None or current.next is None:
            return
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        print("Remove Duplicates from Sorted List =>")
        self.printList()

    # Remove duplicates from a sorted linked list
    def removeDuplicatesUnsorted(self):
        current = self.head
        if current is None or current.next is None:
            return
        newHash = set()
        newHash.add(current.data)
        while current.next:
            if current.next.data in newHash:
                current.next = current.next.next
            else:
                newHash.add(current.next.data)
                current = current.next
        # just for print start
        print("Remove Duplicates from Unsorted List =>")
        self.afterPrintList(self.head)
        # just for print end
        return self.head


if __name__ == "__main__":

    llist = LinkedList()
    llist.push(25)
    llist.push(20)
    llist.push(17)
    llist.push(10)
    llist.push(25)
    llist.push(45)
    llist.push(25)
    llist.push(17)
    llist.push(25)
    llist.printList()
    # llist.removeElementByKeyDummyNode(llist.head, 25)
    llist.removeElementByKeyIterative(25)
    # llist.removeDuplicatesUnsorted()
    print("-"*50)
    slist = LinkedList()
    slist.push(80)
    slist.push(75)
    slist.push(60)
    slist.push(55)
    slist.push(45)
    slist.push(15)
    slist.push(15)
    slist.push(15)
    slist.push(15)
    slist.printList()
    slist.removeDuplicatesSorted()
    # slist.removeDuplicatesUnsorted()


    
