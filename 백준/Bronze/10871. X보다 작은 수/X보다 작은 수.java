import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), x = sc.nextInt();
        int[] arr = new int[a];

        for (int i = 0; i < a; i++) {
            arr[i] = sc.nextInt();
        }

        sc.close();

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < x) {
                System.out.print(arr[i] + " ");
            }
        }
    }
}
