import java.util.*;


class Main {
    
    public static void print(int n){
        if(n == 0) return;
        System.out.println(n);
        print(n-1);
        System.out.println(n);
    }
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number ");
        int n = sc.nextInt();
        print(n);


    }
}