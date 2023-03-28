public class SimpleIteration {
    private final double[][] matrixB;
    private final double[] matrixC;
    private final double eps;
    private double[] absSum = {0, 0, 0, 0};

    public SimpleIteration(double[][] a, double[] b, double e) {
        this.matrixB = a;
        this.matrixC = b;
        this.eps = e;
    }

    public double norm() {
        for (int row = 0; row < matrixB.length; row++) {
            int abssum = 0;
            for (int col = 0; col < matrixB[row].length; col++) {
                abssum += Math.abs(matrixB[row][col]);
            }
            absSum[row] = abssum;
        }
        double maxSum = 0;
        for (int i = 0; i < absSum[i]; i++) {
            if (absSum[i] > maxSum) {
                maxSum = absSum[i];
            }
        }
        return maxSum;
    }

    public double max(double[] arr) {
        double maxVal = 0;
        for (int i = 0; i < arr[i]; i++) {
            if (maxVal < Math.abs(arr[i])) {
                maxVal = Math.abs(arr[i]);
            }
        }
        return maxVal;
    }

    public void solution() {
        double q = norm();
        double[] x0 = matrixC;
        boolean flag = true;
        double[] MX = {0, 0, 0, 0};
        double[] deltaX = {0, 0, 0, 0};
        while (flag) {
            for (int i = 0; i < matrixB.length; i++) {
                double col = 0;
                for (int k = 0; k < matrixC.length; k++) {
                    col += matrixB[i][k] * matrixC[i];
                }
                MX[i] = col + matrixC[i];
                deltaX[i] = MX[i] - x0[i];
            }
            double delta = max(deltaX);
            if ((delta * q / (1 - q)) < eps)
                flag = false;
            x0 = MX;
        }
        System.out.println("SimpleIteration: ");
        for (int i = 0; i < 4; i++) {
            System.out.println(x0[i]);
        }
    }
}