import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 1; i <= t; i++) {
            int a = sc.nextInt(), b = sc.nextInt();
            if (a > b) {
                System.out.printf("#%d >\n", i);
            } else if (a < b) {
                System.out.printf("#%d <\n", i);
            } else if (a == b) {
                System.out.printf("#%d =\n", i);
            }
        }
    }
}
