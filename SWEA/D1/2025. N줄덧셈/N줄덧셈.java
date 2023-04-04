import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int sum = 0;

        for (int i = 1; i <= t; i++) {
            sum += i;
        }
        System.out.println(sum);
    }
}
