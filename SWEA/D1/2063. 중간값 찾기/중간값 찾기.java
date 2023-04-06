import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int[] arr = new int[t];

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            arr[i] += n;
        }
        Arrays.sort(arr);
        System.out.println(arr[t / 2]);
    }
}
