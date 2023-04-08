import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 1; i <= t; i++) {
            int[] num = new int[10];

            for (int j = 0; j < 10; j++) {
                num[j] = sc.nextInt();
            }
            Arrays.sort(num);
            System.out.printf("#%d %d\n", i, num[9]);
        }
    }
}
