import java.util.Scanner;

public class VowelsCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a String: ");
        String inputString = scanner.nextLine().toLowerCase();
        int acount = 0, ecount = 0, icount = 0, ocount = 0, ucount = 0;
        for (int i = 0; i < inputString.length(); i++) {
            char c = inputString.charAt(i);
            switch (c) {
                case 'a': acount++; break;
                case 'e': ecount++; break;
                case 'i': icount++; break;
                case 'o': ocount++; break;
                case 'u': ucount++; break;
            }
        }
        int totalVowels = acount + ecount + icount + ocount + ucount;
        System.out.println("\nVowels Counts:");
        System.out.println("a : " + acount);
        System.out.println("e : " + ecount);
        System.out.println("i : " + icount);
        System.out.println("o : " + ocount);
        System.out.println("u : " + ucount);
        System.out.println("Total : " + totalVowels);
        scanner.close();
    }
}
