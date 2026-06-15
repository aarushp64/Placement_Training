class Smartphone {
    String brand;
    String model;
    int storage;

    // No-arg constructor
    public Smartphone() {
        this.brand = "Unknown";
        this.model = "Generic";
        this.storage = 128;
        System.out.println("No-arg constructor called");
    }

    // Parameterised constructor
    public Smartphone(String brand, String model, int storage) {
        this.brand = brand;
        this.model = model;
        this.storage = storage;
        System.out.println("Parameterised constructor called");
    }

    public void display() {
        System.out.println("Specs: " + brand + " | " + model + " | " + storage + "GB");
    }
}

public class SmartphoneConstructors {
    public static void main(String[] args) {
        System.out.println("== Object Creation ==");

        System.out.println("No-arg:");
        Smartphone s1 = new Smartphone();
        s1.display();

        System.out.println("Parameterised:");
        Smartphone s2 = new Smartphone("Samsung", "S23 Ultra", 512);
        s2.display();

        System.out.println("Another Parameterised:");
        Smartphone s3 = new Smartphone("Vivo", "iQOO 10R", 256);
        s3.display();
    }
}
