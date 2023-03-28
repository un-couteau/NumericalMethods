public class TrapezeAndSimpsonRule {
    private final double[] x;
    private final double[] y;

    public TrapezeAndSimpsonRule(double[] x, double[] y) {
        this.x = x;
        this.y = y;
    }

    public double trapezeRule() {
        double sum = 0.0;
        for (int i = 0; i < x.length - 1; i++) {
            double h = x[i + 1] - x[i];
            sum += (y[i] + y[i + 1]) * h / 2;
        }
        return sum;
    }

    public double simpsonRule() {
        double sum = 0.0;
        for (int i = 0; i < x.length - 2; i += 2) {
            double h = x[i + 2] - x[i];
            sum += (y[i] + 4 * y[i + 1] + y[i + 2]) * h / 6;
        }
        return sum;
    }
}
