public class RectangleRule {
    private final double[] x;
    private final double[] y;

    public RectangleRule(double[] x, double[] y) {
        this.x = x;
        this.y = y;
    }

    public double leftRectangleRule() {
        double sum = 0.0;
        for (int i = 0; i < x.length - 1; i++) {
            double h = x[i + 1] - x[i];
            sum += y[i] * h;
        }
        return sum;
    }

    public double rightRectangleRule() {
        double sum = 0.0;
        for (int i = 1; i < x.length; i++) {
            double h = x[i] - x[i - 1];
            sum += y[i] * h;
        }
        return sum;
    }
}
