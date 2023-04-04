import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int num = 1;

        for (int test_case = 1; test_case <= t + 1; test_case++) {
            System.out.print(num + " ");
            num *= 2;
        }
    }
}
