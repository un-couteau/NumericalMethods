public class Main {
    public static void main(String[] args) {
        double[][] matrixB = {
                {0.17, 0.26, -0.11, -0.16},
                {0.13, -0.12, 0.09, -0.06},
                {0.12, 0.05, -0.03, 0.12},
                {0.13, 0.18, 0.24, 0.45}};

        double[] matrixC = {-1.41, 0.48, -2.38, 0.72};
        double eps = 0.0001;

        Zeidel zeidel = new Zeidel(matrixB, matrixC, eps);
//        zeidel.solution();

        System.out.println();

        SimpleIteration simpleIteration = new SimpleIteration(matrixB, matrixC, eps);
        simpleIteration.solution();
    }

}
