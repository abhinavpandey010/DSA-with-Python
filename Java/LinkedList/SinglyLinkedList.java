package Java.LinkedList;


class SinglyLinkedList {
    Node head;
    Node tail;
    int size = 0;

    public SinglyLinkedList() {
        head = null;
        tail = null;
    }

    void insertAtFirst(int value) {
        Node temp = new Node(value);
        if (head == null) {
            head = temp;
            head.data = value;
            head.next = null;
            tail = head;
        } else {
            temp.next = head;
            head = temp;
        }
        size++;
    }
    void insertAtLast(int value){
        Node temp = new Node(value);
        if(head == null){
            head = temp;
            head.data = value;
            head.next = null;
            tail = head;
        }
        else{
            tail.next = temp;
            tail = temp;
        }
        size++;
    }
    void insertAtIndex(int index,int value){
        Node temp = new Node(value);
        if(index > size - 1){
            System.err.println("Index Out of Bound");
            return;
        }
        Node newTemp = head;
        for(int i = 0;i < index - 1;i++){
            newTemp = newTemp.next;
        }
        temp.next = newTemp.next;
        newTemp.next = temp;
        size++;
    }
    void deleteNode(int value){
        if(head == null){
            System.out.println("Empty LinkedList");
            return;
        }
        if(head.data == value){
            head = head.next;
            return;
        }
        
        Node temp = head;
        Node prev = null;
        while(temp.data != value){
            prev = temp;
            temp = temp.next;
        }
        prev.next = temp.next;
        System.out.println("\n"+temp.data + " deleted");
        size--;
    }
    void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.print("Null");
    }

}
