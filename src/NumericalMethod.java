public class NumericalMethod
{
    private final double a;
    private final double b;
    private final double e;


    public NumericalMethod(double a, double b, double e)
    {
        this.a = a;
        this.b = b;
        this.e = e;
    }

    private double getFunction1(double variable)
    {
        return Math.cos(variable) - Math.pow(variable, 3) + 2;
//        return 3 * Math.sin(variable) - Math.pow(variable, 2) + 4;
    }

    private double getFunction2(double variable)
    {
        return Math.pow(Math.cos(variable) + 2, 0.33333);
    }

    private double getFunction3(double variable)
    {
        return Math.sin(variable) + (3 * Math.pow(variable, 2));
//        return 3 * Math.cos(variable) - 2 * variable;
    }

    public double dichotomyMethod()
    {
        double a = this.a;
        double b = this.b;
        double x = 0;

        while (Math.abs(a - b) > this.e)
        {
            x = (a + b) / 2;

            if (getFunction1(x) * getFunction1(b) < 0)
            {
                a = x;
            }
            else
            {
                b = x;
            }
        }

        return x;
    }

    public double hitoringMethod()
    {
        double x = 0;
        double x0 = (a + b) / 2;


        while (Math.abs(x - x0) > this.e)
        {
            x0 = x;
            x = getFunction2(x0);
        }

        return x;
    }

    public double newtonMethod()
    {
        double b = this.b;
        double a = (this.a + b) / 2;
        double c = a + getFunction1(a) / getFunction3(a);

        while (Math.abs(c - a) > this.e)
        {
            a = c;
            c = a + getFunction1(a) / getFunction3(a);
        }

        return c;
    }

    public double chrodMethod()
    {
        double a = this.a;
        double b = this.b;
        double c = b - ((b - a) / (getFunction1(b) - getFunction1(a))) * getFunction1(b);

        while (Math.abs(c - a) > this.e)
        {
            a = c;
            c = b - ((b - a) / (getFunction1(b) - getFunction1(a))) * getFunction1(b);
        }

        return c;
    }
}
