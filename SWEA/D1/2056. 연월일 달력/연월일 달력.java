import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        int[] daysOfMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 1; i <= t; i++) {
            String s = sc.next();
            int month = Integer.valueOf(s.substring(4, 6));
            int day = Integer.valueOf(s.substring(6, 8));
            String res = "-1";

            if (1 <= month && month <= 12 && 1 <= day && day <= daysOfMonth[month - 1]) {
                res = String.format("%s/%s/%s", s.substring(0,4), s.substring(4,6), s.substring(6,8));
            }
            System.out.format("#%d %s\n", i, res);
        }
    }
}
