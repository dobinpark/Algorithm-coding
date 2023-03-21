import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        int[] count = new int[26];

        for (int i = 0; i < 26; i++) {
            count[i] = str.indexOf(97 + i);
            System.out.print(count[i] + " ");
        }
        sc.close();
    }
}
