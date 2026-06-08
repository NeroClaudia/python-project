package transportation;

public class Bus {

    private int passengerCount;
    private int capacity;

    public Bus(int passengerCount, int capacity) {
        this.passengerCount = passengerCount;
        this.capacity = capacity;
    }

    public int getPassengetCount() {
        return passengerCount;
    }

    public int getCapacity() {
        return capacity;
    }

    public int countTrips(int passengers, int capacity) {
        if (passengers <= 0) {
            return 0;
        }else {
            return 1 + countTrips(passengers - capacity, capacity);
        }
    }
}