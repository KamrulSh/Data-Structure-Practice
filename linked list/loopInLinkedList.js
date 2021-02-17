// javascript program to detect loop
// in the linked list

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    pushItem(new_data) {
        let new_node = new Node(new_data);
        new_node.next = this.head;
        this.head = new_node;
    }

    printList() {
        let temp = this.head;
        while (temp) {
            print(temp.data, (end = " "));
            temp = temp.next;
        }
    }
    detectLoopUsingHash() {
        let s = new Set();
        let temp = this.head;
        while (temp) {
            if (s.has(temp)) return true;
            s.add(temp);

            temp = temp.next;
            console.log(s, temp);
        }
        return False;
    }

    detectLoopUsingFloyd() {
        let slow = this.head,
            fast = this.head;
        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow === fast) return true;
        }
        return false;
    }
}
let llist = new LinkedList();
llist.pushItem(20);
llist.pushItem(4);
llist.pushItem(15);
llist.pushItem(10);
llist.head.next.next.next.next = llist.head;

if (llist.detectLoopUsingFloyd()) console.log("Loop found");
else console.log("No Loop ");
