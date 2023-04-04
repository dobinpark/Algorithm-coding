import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int p = sc.nextInt(), k = sc.nextInt();
        int cut = 0;

        for (int i = k; i <= p; i++) {
            cut += 1;
        }
        System.out.println(cut);
    }
}
