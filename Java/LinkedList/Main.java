package Java.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.insertAtFirst(5);
        ll.insertAtFirst(6);
        ll.insertAtFirst(7);
        ll.insertAtFirst(8);
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

    public LinkedList() {
        head = null;
    }

    void insertAtFirst(int value) {
        Node temp = new Node(value);
        if (head == null) {
            head = temp;
            head.data = value;
            head.next = null;
        } else {
            temp.next = head;
            head = temp;
        }

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