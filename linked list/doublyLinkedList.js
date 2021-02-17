class Node {
    constructor(value, prev, next) {
        this.value = value;
        this.prev = prev || null;
        this.next = next || null;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = this.tail = null;
        this.count = 0;
    }

    append(value) {
        let newNode = new Node(value);
        this.count++;
        if (!this.tail) {
            this.head = this.tail = newNode;
        } else {
            let oldTail = this.tail;
            this.tail = newNode;
            oldTail.next = this.tail;
            this.tail.prev = oldTail;
        }
    }

    prepend(value) {
        let newNode = new Node(value);
        this.count++;
        if (!this.head) {
            this.head = this.tail = newNode;
        } else {
            let oldHead = this.head;
            this.head = newNode;
            this.head.next = oldHead;
            oldHead.prev = this.head;
        }
    }

    deleteHead() {
        if (!this.head) {
            return null;
        } else {
            let removedHead = this.head;
            this.count--;
            if (this.head === this.tail) {
                this.head = this.tail = null;
            } else {
                this.head = this.head.next;
                this.head.prev = null;
            }
            return removedHead.value;
        }
    }

    deleteTail() {
        if (!this.tail) {
            return null;
        } else {
            let removedTail = this.tail;
            this.count--;
            if (this.head === this.tail) {
                this.head = this.tail = null;
            } else {
                this.tail = this.tail.prev;
                this.tail.next = null;
            }
            return removedTail.value;
        }
    }

    searchValue() {
        let currentNode = this.head;
        while (currentNode) {
            if (currentNode.value === value) {
                return currentNode;
            }
            currentNode = currentNode.next;
        }
    }
}

let doubly = new DoublyLinkedList();
doubly.append(23);
doubly.append(44);
doubly.append(55);
doubly.append(66);
doubly.prepend(-77);
doubly.prepend(87);
doubly.prepend(97);
doubly.deleteHead();
doubly.deleteTail();
console.log(doubly);
