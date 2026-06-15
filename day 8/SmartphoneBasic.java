class SmartphoneBasic {
    public boolean isOn;
    public int brightness;

    public void turnOn() {
        isOn = true;
        brightness = 100;
    }

    public void status() {
        System.out.println("Brightness Status: " + (isOn ? "ON" : "OFF") + " at " + brightness + "%");
    }
}

public class SmartphoneBasicMain {
    public static void main(String[] args) {
        SmartphoneBasic phone = new SmartphoneBasic();
        phone.turnOn();
        phone.status();
    }
}
