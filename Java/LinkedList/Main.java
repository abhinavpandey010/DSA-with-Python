package Java.LinkedList;

public class Main {
    public static void main(String[] args) {
        // SinglyLinkedList ll = new SinglyLinkedList();
        // ll.insertAtFirst(5);
        // ll.insertAtFirst(6);
        // // ll.insertAtFirst(7);
        // // ll.insertAtFirst(8);
        // ll.insertAtLast(8);
        // ll.insertAtLast(9);
        // ll.insertAtLast(10);
        // ll.insertAtIndex(2, 12);
        // ll.display();
        // ll.deleteNode(10);
        // ll.display();

        DoublyLinkedList dll = new DoublyLinkedList();
        dll.insertAtFirst(5);
        dll.insertAtFirst(6);
        dll.insertAtFirst(7);
        dll.insertAtFirst(8);
        dll.insertAtLast(10);
        dll.insertAtLast(12);
        dll.insertAtLast(11);
        dll.insertAtIndex(2, 45);
        // dll.display();
        // dll.deleteNode(11);
        dll.display();


    }
}

//singly linked list
class Node {
    int data;
    Node next;
    Node prev;

    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}
// class Node {
//     int data;
//     Node next;
  

//     public Node(int data) {
//         this.data = data;
//         this.next = null;

//     }
// }

