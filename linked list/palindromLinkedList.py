# Function to check if a singly linked list is palindrome

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

    def printListOp(self, head):
        current = head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("null")

    # method 1 -> stack method
    # Time and space complexity: O(n)
    def checkPalindromUsingStack(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        current = self.head
        isPalindrome = True
        while current:
            peak = stack.pop()
            if peak == current.data:
                isPalindrome = True
            else:
                isPalindrome = False
                break
            current = current.next
        if isPalindrome:
            print("List is palindrome\n")
        else:
            print("List is not palindrome\n")

    # METHOD 2 (By reversing the list)
    # Time Complexity: O(n) Auxiliary Space: O(1)
    def checkPalindromByReverseList(self):
        # find middle element
        slow = fast =self.head
        self.printList()
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the 2nd half list
        middleHead = slow
        previous = None
        tempHead = None
        while middleHead:
            tempHead = middleHead.next
            middleHead.next = previous
            previous = middleHead
            middleHead = tempHead
        # for print start
        reverse = previous
        print("After reverse:")
        self.printListOp(reverse)
        # for print end
        current = self.head
        isPalindrome = True
        while current and reverse:
            if current.data != reverse.data:
                isPalindrome = False
                break
            else:
                current = current.next
                reverse = reverse.next
        
        if isPalindrome:
            print("List is palindrome")
        else:
            print("List is not palindrome")


    

if __name__ == "__main__":
    llist = LinkedList()
    nlist = [30, 40, 50, 60, 50, 40, 30]
    for i in range(len(nlist)):
        llist.appendAtHead(nlist[i])
    llist.checkPalindromByReverseList()
    print("-"*50)

    ll = LinkedList()
    sl = [ 'a', 'b', 'a', 'c', 'a', 'b', 'a' ]
    for i in range(len(sl)):
        ll.appendAtHead(sl[i])
        ll.printList()
        ll.checkPalindromUsingStack()
