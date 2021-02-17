# singly linked list implementation using head and tail

class ListNode:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
      
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        
        if index<0 or index >= self.size:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.value
        

    def addAtHead(self, val: int) -> None:
        
        newNode = ListNode(val)
        if self.head is None:
            self.head = self.tail = newNode
        else: 
            newNode.next = self.head
            self.head = newNode
        self.size += 1
        
        

    def addAtTail(self, val: int) -> None:
        
        newNode = ListNode(val)
        if self.tail is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index>self.size: 
            return
        elif index <= 0: 
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            newNode = ListNode(val)    
            current = self.head
            for i in range(index-1):
                current = current.next
            newNode.next = current.next
            current.next = newNode
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        
        current = self.head
        if index < 0 or index >= self.size or not self.head:
            return -1
        elif index == 0:
            self.head = current.next
        else:
            for _ in range(index-1):
                current = current.next
                
            current.next = current.next.next
            if current.next is None:
                self.tail = current
        self.size -= 1

    def printList(self) -> None:
        current = self.head
        while current:
            print(current.value)
            current = current.next
        


# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyLinkedList()
    param_1 = obj.get(1)
    obj.addAtHead(22)
    obj.addAtTail(33)
    obj.addAtIndex(2,55)
    obj.deleteAtIndex(3)
    obj.printList()