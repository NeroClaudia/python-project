package transportation;

public class Bicycle {

    private int wheelSize;

    public Bicycle(int wheelSize) {
        this.wheelSize = wheelSize;
    }

    public int getWheelSize() {
        return wheelSize;
    }

    public double maxDistance() {
        return wheelSize * 20;
    }

    public double wheelArea() {
        return Math.PI * wheelSize * wheelSize;
    }
}