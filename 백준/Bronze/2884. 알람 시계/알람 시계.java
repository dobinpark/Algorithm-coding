import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();

        if ((H < 0 || H > 24) && (M < 0 || M > 60)) {
            System.out.println("error");
        }
        else if (M >= 45) {
            M -= 45;
            System.out.println(H + " " + M);
        }
        else if (H != 0 && M < 45) {
            H -= 1;
            M = (60 + (M - 45));
            System.out.println(H + " " + M);
        }
        else if (H == 0 && M  < 45) {
            H = 23;
            M = (60 + (M - 45));
            System.out.println(H + " " + M);
        }

        sc.close();
    }
}