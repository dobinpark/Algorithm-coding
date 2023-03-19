import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        double[] arr = new double[N];
        double max = -987654321, M = 0;

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
            if (max < arr[i]) {
                max = arr[i];
            }
        }
        
        for (int i = 0; i < N; i++) {
            M += arr[i] / max * 100.0;
        }
        System.out.println(M / N);
    }
}
