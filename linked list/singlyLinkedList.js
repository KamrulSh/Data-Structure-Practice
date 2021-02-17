// linked list implementation using head

class Node {
    constructor(element) {
        this.element = element;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    addElement(element) {
        let node = new Node(element);
        let current;
        if (this.head == null) {
            this.head = node;
        } else {
            current = this.head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = node;
        }
        console.log(element, "added at index", this.indexOf(element));
        this.size++;
    }

    insertElementAt(index, element) {
        if (index < 0 || index > this.size) {
            return console.log(element, "can't insert");
        } else {
            let node = new Node(element);
            let current, previous;
            if (index == 0) {
                node.next = this.head;
                this.head = node;
            } else {
                let iteration = 0;
                current = this.head;
                while (iteration < index) {
                    iteration++;
                    previous = current;
                    current = current.next;
                }
                node.next = current;
                previous.next = node;
            }
        }
        console.log(element, "added at new index", index);
        this.size++;
    }

    removeElementFrom(index) {
        if (index < 0 || index >= this.size) {
            return console.log(index, "index can't remove");
        } else {
            let current = this.head,
                previous;
            if (index == 0) {
                this.head = current.next;
            } else {
                let iteration = 0;
                while (iteration < index) {
                    iteration++;
                    previous = current;
                    current = current.next;
                }
                previous.next = current.next;
            }
            this.size--;
            console.log(current.element, "removed");
            return current.element;
        }
    }

    removeElement(element) {
        let current = this.head;
        let previous = null;
        while (current != null) {
            if (current.element === element) {
                if (previous === null) {
                    this.head = current.next;
                } else {
                    previous.next = current.next;
                }
                console.log(element, "removed");
                this.size--;
                return current.element;
            }
            previous = current;
            current = current.next;
        }
        console.error(element, "not found");
        return -1;
    }

    indexOf(element) {
        let current = this.head;
        let count = 0;
        while (current != null) {
            if (current.element === element) {
                return count;
            }
            count++;
            current = current.next;
        }
        return count;
    }

    isEmpty() {
        return this.size === 0;
    }

    sizeOfList() {
        return this.size;
    }

    printList() {
        let current = this.head;
        let str = "";
        while (current) {
            str += current.element + " ";
            current = current.next;
        }
        console.log("All items: ", str);
    }

    printListWithIndex() {
        let current = this.head;
        while (current != null) {
            console.log(this.indexOf(current.element), "=>", current.element);
            current = current.next;
        }
    }
}

let ll = new LinkedList();
console.log("isEmpty:", ll.isEmpty(), ", size:", ll.sizeOfList());
ll.addElement(23);
ll.addElement(56);
ll.addElement(223);
ll.addElement(356);
ll.insertElementAt(0, 100);
ll.insertElementAt(1, 200);
ll.insertElementAt(6, 99);
ll.printListWithIndex();
ll.printList();
ll.removeElementFrom(0);
ll.removeElement(56);
ll.printList();
console.log("isEmpty:", ll.isEmpty(), ", size:", ll.sizeOfList());
ll.printListWithIndex();
console.log(ll);
