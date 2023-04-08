import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            float sum = 0;
            for (int j = 0; j < 10; j++) {
                int num = sc.nextInt();
                sum += num;
            }
            System.out.printf("#%d %d\n", i + 1, Math.round(sum / 10));
        }
    }
}
