import java.util.Scanner;

public class AgeClassifier {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        if (age <= 5) {
            System.out.println("Baby");
        } else if (age > 5 && age <= 12) {
            System.out.println("Child");
        } else if (age >= 12 && age <= 19) {
            System.out.println("Teenage");
        } else if (age >= 19 && age <= 50) {
            System.out.println("Adult");
        } else if (age >= 51 && age <= 60) {
            System.out.println("Retirement");
        } else {
            System.out.println("Swargaat bhetu");
        }
        scanner.close();
    }
}
