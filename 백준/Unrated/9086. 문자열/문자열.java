import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            String n = sc.next();
            int str = n.length();
            System.out.print(String.valueOf((n.charAt(0))));
            System.out.println(String.valueOf((n.charAt(str - 1))));
        }
    }
}
