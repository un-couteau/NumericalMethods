public class Gauss {
    public static void main(String[] args) {
        int a = 0; // нижний предел интегрирования
        int b = 2; // верхний предел интегрирования
        int n = 5; // количество узлов
        double[] x = {-0.9061798, -0.5384693, 0.0, 0.5384693, 0.9061798}; // узлы
        double[] w = {0.2369269, 0.4786287, 0.5688889, 0.4786287, 0.2369269}; // веса

        double sum = 0.0;
        for (int i = 0; i < n; i++) {
            double t = ((b - a) / 2.0) * x[i] + ((a + b) / 2.0); // замена переменной
            sum += w[i] * f(t); // вычисление интеграла
        }
        double gaussIntegral = ((b - a) / 2.0) * sum;
        System.out.println("Gauss's method with n=5: " + gaussIntegral);
    }

    public static double f(double x) {
        return Math.pow(1 + Math.pow(x, 2), -1); // подынтегральная функция
    }
}
