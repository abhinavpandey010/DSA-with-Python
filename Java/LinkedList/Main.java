package Java.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.insertAtFirst(5);
        ll.insertAtFirst(6);
        // ll.insertAtFirst(7);
        // ll.insertAtFirst(8);
        ll.insertAtLast(8);
        ll.insertAtLast(9);
        ll.insertAtLast(10);
        ll.insertAtIndex(2, 12);
        ll.display();

    }
}

class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    Node head;
    Node tail;
    int size = 0;

    public LinkedList() {
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
    void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.print("Null");
    }

}