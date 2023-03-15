import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int N;
		
		N = input.nextInt();
	
		for(int i = 0; i < N; i++) {
			for(int j = N-i-1; j > 0; j--) {
				System.out.print(" ");
			}
			for(int k = 1; k < i+2; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
		input.close();
	}
}