public class TypesCasting {
    public static void main(String[] args) {
        System.out.println("String to int");
        String numString = "1235";
        int n1 = Integer.parseInt(numString);
        System.out.println("parseInt way: " + n1 + " (math check: " + (n1 + 1) + ")");
        int n2 = Integer.valueOf(numString);
        System.out.println("valueOf way: " + n2 + " (math check: " + (n2 + 1) + ")");
        String invalidString = "123abc";
        try {
            int badNumber = Integer.parseInt(invalidString);
        } catch (NumberFormatException e) {
            System.out.println("Error: cannot convert " + invalidString + " to int");
        }
    }
}
