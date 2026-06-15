import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner scanner = new Scanner(System.in);
        int numberToGuess = rand.nextInt(100) + 1;
        int numberOfTries = 0;
        int guess;
        boolean hasGuessedCorrectly = false;
        System.out.println("Welcome to the Guessing Game!");
        System.out.println("I have selected a number between 1 and 100.");
        System.out.println("Can you guess the number?");
        while (!hasGuessedCorrectly) {
            System.out.print("Enter a number: ");
            guess = scanner.nextInt();
            numberOfTries++;
            if (guess < numberToGuess) {
                System.out.println("Too low! Try again.");
            } else if (guess > numberToGuess) {
                System.out.println("Too high! Try again.");
            } else {
                hasGuessedCorrectly = true;
                System.out.println("Correct! You guessed it in " + numberOfTries + " tries.");
            }
        }
        scanner.close();
    }
}
