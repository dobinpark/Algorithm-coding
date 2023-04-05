import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        String t = sc.next();
        String[] eng = t.split("");

        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String alpha[] = alphabet.split("");

        for (int i = 0; i < eng.length; i++) {
            for (int j = 0; j < 26; j++) {
                if (eng[i].equals(alpha[j])) {
                    System.out.print((j + 1) + " ");
                }
            }
        }
    }
}
