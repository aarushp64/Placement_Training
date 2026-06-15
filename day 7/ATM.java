public class ATM {
    public static void main(String[] args) {
        int amount = 5785;
        int[] denominations = {500, 200, 100, 50, 20, 10, 5};
        System.out.println("Breakdown for Amount: $" + amount);
        for (int note : denominations) {
            int count = amount / note;
            amount %= note;
            if (count > 0) {
                System.out.println("$" + note + "x" + count);
            }
        }
        if (amount > 0) {
            System.out.println("Remaining Amount");
        }
    }
}
