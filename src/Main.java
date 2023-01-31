public class Main
{
    public static void main(String[] args)
    {
        NumericalMethod numericalMethod = new NumericalMethod(0, 2, Math.pow(10, -3));
        System.out.printf("Dichotomy method result: %s%n" +
                        "Hitoring method result: %s%n" +
                        "Newton method result: %s%n",
                numericalMethod.dichotomyMethod(),
                numericalMethod.hitoringMethod(),
                numericalMethod.newtonMethod()
                );
    }
}