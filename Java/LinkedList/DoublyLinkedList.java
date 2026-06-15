package Java.LinkedList;

public class DoublyLinkedList {
    Node head;
    Node tail;
    int size  = 0;
    public DoublyLinkedList(){
        head = null;
        tail = null;
    }
    void insertAtFirst(int value){
        Node temp = new Node(value);
        if(head == null){
            head = temp;
            tail = temp;
        }
        else{
            head.prev = temp;
            temp.next = head;
            head = temp;
        }
        size++;
    }
    void insertAtLast(int value){
        Node temp = new Node(value);
        if(head == null){
            head = temp;
            tail = temp;
        }
        else{
            tail.next = temp;
            temp.prev = tail;
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
        for(int i = 0;i < index;i++){
            newTemp = newTemp.next;
        }
        temp.next = newTemp;
        temp.prev = newTemp.prev;
        newTemp.prev = temp;
        size++;
    }
    void deleteNode(int value){
        if(head == null){
            System.out.println("Empty LinkedList");
            return;
        }
        if(head.data == value){
            head = head.next;
            head.prev = null;
            return;
        }
        if(tail.data == value){
            tail = tail.prev;
            tail.next = null;
            return;
        }
        Node temp = head;
        Node prevNode = null;
        Node nextNode = null;
        while(temp.data != value){
            prevNode = temp;
            temp = temp.next;
            nextNode = temp.next;
        }
        prevNode.next = nextNode;
        nextNode.prev = temp.prev;
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
