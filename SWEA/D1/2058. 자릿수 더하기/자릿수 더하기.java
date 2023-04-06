import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        int result = 0;

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t > 10) {
            result += t % 10;
            t = t/ 10;
        }
        System.out.println(result + t);
    }
}
