class DeliveryVehicle {
    String vehicleId;

    public DeliveryVehicle(String vehicleId) {
        this.vehicleId = vehicleId;
    }

    public void dispatch() {
        System.out.println("Vehicle " + vehicleId + " is moving");
    }
}

class DroneDelivery extends DeliveryVehicle {
    public DroneDelivery(String vehicleId) {
        super(vehicleId);
    }

    @Override
    public void dispatch() {
        System.out.println("Drone " + vehicleId + " is moving");
    }
}

class LogisticManager {
    public void scheduleDelivery(String address) {
        System.out.println("Standard delivery scheduled to " + address);
    }

    public void scheduleDelivery(String address, String timeSlot) {
        System.out.println("Standard delivery scheduled to " + address + " during time slot " + timeSlot);
    }

    public void scheduleDelivery(int trackingId) {
        System.out.println("Querying tracking ID: " + trackingId);
    }
}

public class OverloadingOverriding {
    public static void main(String[] args) {
        System.out.println("----- Overloading -----");
        LogisticManager manager = new LogisticManager();
        manager.scheduleDelivery("123 Loni Kalbhor, Pune");
        manager.scheduleDelivery("Santa, Mumbai", "4PM - 8PM");
        manager.scheduleDelivery(346985);

        System.out.println("----- Overriding -----");
        DeliveryVehicle van = new DeliveryVehicle("Van1");
        van.dispatch();
        DeliveryVehicle drone = new DroneDelivery("Drone1");
        drone.dispatch();
    }
}
