# Function to find intersection point

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

    def countLength(self, head):
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # method 1 : making same length
    # Time Complexity: O(m+n) 
    # Auxiliary Space: O(1)
    # find the intersection Point of the two lists
    def findIntersectionPoint(self, llist1, llist2):
        length1 = self.countLength(llist1.head)
        length2 = self.countLength(llist2.head)
        print(length1, length2)
        diffLength = abs(length1 - length2)

        current1 = llist1.head
        current2 = llist2.head
        if length1 > length2:
            for i in range(diffLength):
                current1 = current1.next
        else:
            for i in range(diffLength):
                current2 = current2.next
        
        while current1 and current2:
           # here we are checking the value of the nodes
           # but we have to check nodes instead 
            if current1.data == current2.data:
                print("intersection point is:", current1.data)
                return current1.data
            else:
                current1 = current1.next
                current2 = current2.next
        print("no intersection point found")
        return None


if __name__ == "__main__":
    llist1 = LinkedList()
    nlist1 = [90, 80, 70, 60, 50, 30, 10]
    # nlist1 = []
    for i in range(len(nlist1)):
        llist1.appendAtHead(nlist1[i])
    llist1.printList()

    llist2 = LinkedList()
    # nlist2 = [90, 85, 75, 65, 45, 35, 25, 15]
    nlist2 = [90, 80, 70, 60, 50, 30, 20, 15]
    # nlist2 = []
    for i in range(len(nlist2)):
        llist2.appendAtHead(nlist2[i])
    llist2.printList()

    llist3 = LinkedList()
    llist3.findIntersectionPoint(llist1, llist2)
