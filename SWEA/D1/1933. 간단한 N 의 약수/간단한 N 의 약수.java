import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int test_case = 1; test_case <= t; test_case++) {
            if (t % test_case == 0) {
                System.out.print(test_case + " ");
            }
        }
    }
}
