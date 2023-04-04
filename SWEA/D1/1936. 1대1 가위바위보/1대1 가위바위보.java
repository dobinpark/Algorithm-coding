import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt();

        if (a > b) {
            System.out.println("A");
        } else if (a < b) {
            System.out.println("B");
        }
    }
}
