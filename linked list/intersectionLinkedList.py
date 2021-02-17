# Intersection of two Sorted Linked Lists
# get the common elements from the lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def appendAtHead(head, value):
    newNode = Node(value)
    newNode.next = head
    head = newNode
    return head

def printList(head):
    current = head
    while current:
        print(current.data, end=' -> ')
        current = current.next
    print("null")

# method: Using Dummy Node
def intersectionOfLinkedList(list1, list2):
    dummy = Node(-1)
    tail = dummy

    while list1 and list2:
        if list1.data == list2.data:
            # tail.next is None
            # then a new node is inserted before tail.next as head
            tail.next = appendAtHead(tail.next, list1.data)
            # move tail to the next node
            tail = tail.next
            list1 = list1.next
            list2 = list2.next
        elif list1.data > list2.data:
            list2 = list2.next
        else:
            list1 = list1.next
    printList(dummy.next)
    return dummy.next
    

if __name__ == "__main__":
    # create the sorted linked list
    list1 = None
    list1 = appendAtHead(list1, 65)
    list1 = appendAtHead(list1, 60)
    list1 = appendAtHead(list1, 57)
    list1 = appendAtHead(list1, 55)
    list1 = appendAtHead(list1, 50)
    list1 = appendAtHead(list1, 45)
    list1 = appendAtHead(list1, 42)
    list1 = appendAtHead(list1, 40)
    list1 = appendAtHead(list1, 30)
    printList(list1)

    list2 = None
    # list2 = appendAtHead(list2, 75)
    list2 = appendAtHead(list2, 65)
    list2 = appendAtHead(list2, 62)
    list2 = appendAtHead(list2, 60)
    list2 = appendAtHead(list2, 55)
    list2 = appendAtHead(list2, 52)
    list2 = appendAtHead(list2, 45)
    list2 = appendAtHead(list2, 30)
    printList(list2)
    intersectionOfLinkedList(list1, list2)
    
