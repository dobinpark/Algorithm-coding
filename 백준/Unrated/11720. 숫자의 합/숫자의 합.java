import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = sc.next();
        int num = 0;

        for (int i = 0; i < n; i++) {
            num += str.charAt(i) - 48;
        }

        System.out.println(num);
    }
}
