package transportation;
import java.util.Scanner;
public class TransportationMain {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int bicycleSize = scanner.nextInt();
        Bicycle b = new Bicycle(bicycleSize);

        int fuelCapacity = scanner.nextInt();
        int mileage = scanner.nextInt();
        Motorcycle m = new Motorcycle(fuelCapacity, mileage);

        int passCount = scanner.nextInt();
        int capacity = scanner.nextInt();
        Bus bus = new Bus(passCount, capacity);

        int travel = 360;

        System.out.println("A is a bicycle with wheel size of " + b.getWheelSize() + ", maximum travel distance of " + b.maxDistance() + " km, and wheel area of " + (Math.round(b.wheelArea() * 10.0) / 10.0) + ".");
        System.out.println();
        System.out.println("B is a motorcycle with fuel capacity of " + m.getFuelCapacity() + ", mileage of " + m.getMileage() + " km/l, and maximum travel distance of " + m.maxDistance() + " km.");
        System.out.println();
        System.out.println("The fuel needed by B to travel " + travel + " km is " + m.fuelNeeded(travel) + " liters.");
        System.out.println();
        System.out.println("C is a bus with passenger count of " + bus.getPassengetCount() + " and capacity of " + bus.getCapacity() + " passengers per trip.");
        System.out.println();
        System.out.println("The minimum number of trips required by C is " + bus.countTrips(passCount, capacity));
        
        scanner.close();
    }
}