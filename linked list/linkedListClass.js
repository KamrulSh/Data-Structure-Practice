class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    makeNode(value) {
        return {
            value: value,
            next: null,
        };
    }

    // add item at the tail of the linked list
    append(item) {
        let node = this.makeNode(item);
        if (!this.head) {
            this.head = this.tail = node;
            this.length++;
            return node;
        }

        this.tail.next = node;
        this.tail = node;
        this.length++;
        return node;
    }

    // add item at the head of the linked list
    prepend(item) {
        let node = this.makeNode(item);
        if (!this.head) {
            this.head = this.tail = node;
            this.length++;
            return node;
        }

        node.next = this.head;
        this.head = node;
        this.length++;
    }

    removeFirstItem() {
        if (!this.head) {
            return null;
        }

        let nodeToRemove = this.head;
        this.head = nodeToRemove.next;
        nodeToRemove.next = null;
        console.log("nn", nodeToRemove);
        if (nodeToRemove === this.tail) {
            this.tail = null;
        }
        this.length--;
        return nodeToRemove;
    }

    findNodeBefore(item) {
        if (!item) {
            return null;
        }
        let current = this.head;
        while (current) {
            if (current.next == item) {
                break;
            }
            current = current.next;
        }
        console.log("current", current);
        return current;
    }

    removeLastItem() {
        if (!this.tail) {
            return null;
        }
        let nodeToRemove = this.tail;
        console.log("nodeToRemove", nodeToRemove);
        this.tail = this.findNodeBefore(this.tail);
        console.log("object", this.tail);
        this.tail = null;
        console.log("rr", this.head);
        if (nodeToRemove === this.head) {
            this.head = null;
        }
        this.length--;
        return nodeToRemove;
    }

    printList() {
        let current = this.head;
        while (current) {
            console.log(current);
            current = current.next;
        }
    }

    getItem() {
        let count = 0;
        let current = this.head;
        while (current) {
            count++;
            current = current.next;
        }
        return count;
    }
}

let newNode = new LinkedList();
console.log("Before", newNode);
newNode.append(4);
newNode.append(43);
newNode.append(44);
newNode.prepend(100);
console.log("After", newNode);
newNode.removeLastItem();
console.log(newNode);
