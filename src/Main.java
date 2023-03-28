public class Main {
    public static void main(String[] args) {
        double[] x = {0.119, 0.121, 0.123, 0.125, 0.127};
        double[] y = {1.30918, 1.32434, 1.33968, 1.35519, 1.37068};


        RectangleRule rectangleRule = new RectangleRule(x, y);
        System.out.println("Left rectangle rule: " + rectangleRule.leftRectangleRule());
        System.out.println("Right rectangle rule: " + rectangleRule.rightRectangleRule());


        TrapezeAndSimpsonRule trapezeAndSimpsonRule = new TrapezeAndSimpsonRule(x, y);
        System.out.println("Trapeze rule: " + trapezeAndSimpsonRule.trapezeRule());
        System.out.println("Simpson rule: " + trapezeAndSimpsonRule.simpsonRule());
    }
}
