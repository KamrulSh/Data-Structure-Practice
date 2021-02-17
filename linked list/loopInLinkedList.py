# Python3 program to detect loop
# in the linked list

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
        current = self.head
        while(current):
            print(current.data, end="->")
            current = current.next
        print("null")

    # creates a loop by connnecting the last node  
    # to n^th node of the linked list
    def createLoop(self, position):
        loopNode = self.head
        for _ in range(position):
            loopNode = loopNode.next
            loopStart = loopNode
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = loopNode
        print(f"Loop created {currentNode.data} => {loopStart.data}")

    # Solution 1: Hashing Approach: O(n) space
    def detectLoopUsingHash(self):
        if self.head is None:
            return None
        newSet = set()
        current = self.head
        while current:
            if current in newSet:
                print("Loop found")
                return True
            else:
                newSet.add(current)
                current = current.next
        print("No Loop ")
        return False

    # Solution 2: Floyd’s Cycle-Finding Algorithm O(1) space
    def detectLoopUsingFloyd(self):
        if self.head is None:
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Loop found")
                return True
        print("No Loop ")
        return False

    # Find length of loop in linked list using Floyd’s Algorithm
    def countLoopLengthUsingFloyd(self):
        if self.head is None:
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                print("Length of loop is", count)
                return count
        print("No Loop found")
        return False

if __name__ == "__main__":

    llist = LinkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.push(50)
    llist.push(60)
    llist.push(70)
    llist.push(80)
    llist.printList()
    llist.detectLoopUsingHash()
    llist.detectLoopUsingFloyd()
    llist.countLoopLengthUsingFloyd()
    llist.createLoop(3)
    llist.detectLoopUsingHash()
    llist.detectLoopUsingFloyd()
    llist.countLoopLengthUsingFloyd()