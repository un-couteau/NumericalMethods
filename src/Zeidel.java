public class Zeidel {
    private final double[][] matrixB;
    private final double[] matrixC;
    private final double eps;
    private double[] absSum = {0, 0, 0, 0};

    public Zeidel(double[][] matrixB, double[] matrixC, double eps) {
        this.matrixB = matrixB;
        this.matrixC = matrixC;
        this.eps = eps;
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
            ;
        }
        return maxVal;
    }

    public void solution() {
        double q = norm();
        double[] MX = {0.0, 0.0, 0.0, 0.0};
        boolean flag = true;
        int iterations = 0;
        double[] x0 = {matrixC[0], matrixC[1], matrixC[2], matrixC[3]};
        while (flag) {
            x0[0] = x0[0] * matrixB[0][0] + x0[1] * matrixB[0][1] + x0[2] * matrixB[0][2] + matrixC[0];
            x0[1] = x0[0] * matrixB[1][0] + x0[1] * matrixB[1][1] + x0[2] * matrixB[1][2] + matrixC[1];
            x0[2] = x0[0] * matrixB[2][0] + x0[1] * matrixB[2][1] + x0[2] * matrixB[2][2] + matrixC[2];
            x0[3] = x0[0] * matrixB[3][0] + x0[1] * matrixB[3][1] + x0[2] * matrixB[3][2] + matrixC[3];

            double[] deltaX = new double[4];
            for (int i = 0; i < 4; i++) {
                deltaX[i] = x0[i] - MX[i];
            }
            double delta = max(deltaX);
            if ((delta * q / (1 - q)) < eps) {
                flag = false;
            }
            MX[0] = x0[0];
            MX[1] = x0[1];
            MX[2] = x0[2];
            MX[3] = x0[3];
            iterations += 1;
        }
        System.out.println("Zeidel: ");
        for (int i = 0; i < 4; i++) {
            System.out.println(x0[i]);
        }
//        System.out.println(iterations);
    }
}
