// linked list implementation using head and tail

let Node = function (val) {
    this.val = val;
    this.next = null;
};

let MyLinkedList = function () {
    this.head = null;
    this.tail = null;
    this.size = 0;
};

MyLinkedList.prototype.get = function (index) {
    if (index >= this.size || index < 0) return -1;
    let current = this.head;
    for (let i = 0; i < index; i++) {
        current = current.next;
    }
    return current.val;
};

MyLinkedList.prototype.addAtHead = function (val) {
    let newNode = new Node(val);
    if (!this.head) {
        this.head = newNode;
        this.tail = newNode;
    } else {
        newNode.next = this.head;
        this.head = newNode;
    }
    this.size++;
    return this;
};

MyLinkedList.prototype.addAtTail = function (val) {
    let newNode = new Node(val);
    if (!this.tail) {
        this.tail = newNode;
        this.head = newNode;
    } else {
        this.tail.next = newNode;
        this.tail = newNode;
    }
    this.size++;
    return this;
};

MyLinkedList.prototype.addAtIndex = function (index, val) {
    let newNode = new Node(val);
    if (index > this.size) return;
    if (index <= 0) return this.addAtHead(val);
    if (index === this.size) return this.addAtTail(val);

    let current = this.head;
    for (let i = 0; i < index - 1; i++) current = current.next;
    newNode.next = current.next;
    current.next = newNode;
    this.size++;
    return this;
};

MyLinkedList.prototype.deleteAtIndex = function (index) {
    if (index < 0 || index >= this.size) return;
    if (index === 0) {
        this.head = this.head.next;
        this.size--;
        return this;
    }
    let current = this.head;
    for (let i = 0; i < index - 1; i++) current = current.next;
    current.next = current.next.next;
    if (!current.next) {
        this.tail = current;
    }
    this.size--;
    return this;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let obj = new MyLinkedList()
 * let param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
