import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String x = "";
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            x += "*";
            System.out.println(x);
        }
    }
}