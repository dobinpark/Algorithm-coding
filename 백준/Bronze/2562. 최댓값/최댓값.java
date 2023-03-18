import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] arr = new int[9];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        int a = arr[0];

        for (int i = 0; i < arr.length; i++) {
            if (a < arr[i]) {
                a = arr[i];
            }
        }

        System.out.println(a);

        int b = 0;

        for (int i = 0; i < arr.length; i++) {
            b += 1;
            if (a == arr[i]) {
                System.out.println(b);
            }
        }
    }
}
