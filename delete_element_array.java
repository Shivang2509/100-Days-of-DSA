import java.util.Scanner;

public class delete_element_array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        // Input array elements
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int pos = sc.nextInt();

        // Shift elements to the left
        for (int i = pos - 1; i < n - 1; i++) {
            arr[i] = arr[i + 1];
        }

        // Print updated array
        for (int i = 0; i < n - 1; i++) {
            System.out.print(arr[i] + " ");
        }

        sc.close();
    }
}