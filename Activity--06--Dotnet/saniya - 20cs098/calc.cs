using System;

class Calculator
{
    static void Main()
    {
        while (true)
        {
            Console.WriteLine("Simple Calculator");
            Console.WriteLine("1. Addition");
            Console.WriteLine("2. Subtraction");
            Console.WriteLine("3. Multiplication");
            Console.WriteLine("4. Division");
            Console.WriteLine("5. Exit");
            Console.Write("Enter your choice (1/2/3/4/5): ");

            int choice;
            if (int.TryParse(Console.ReadLine(), out choice))
            {
                if (choice >= 1 && choice <= 4)
                {
                    double result = PerformOperation(choice);
                    Console.WriteLine("Result: " + result);
                }
                else if (choice == 5)
                {
                    Console.WriteLine("Exiting the calculator.");
                    break;
                }
                else
                {
                    Console.WriteLine("Invalid choice. Please select a valid option.");
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a number (1/2/3/4/5).");
            }
        }
    }

    static double PerformOperation(int choice)
    {
        double num1, num2;

        Console.Write("Enter the first number: ");
        num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter the second number: ");
        num2 = Convert.ToDouble(Console.ReadLine());

        double result = 0;

        switch (choice)
        {
            case 1:
                result = num1 + num2;
                break;
            case 2:
                result = num1 - num2;
                break;
            case 3:
                result = num1 * num2;
                break;
            case 4:
                if (num2 != 0)
                    result = num1 / num2;
                else
                    Console.WriteLine("Division by zero is not allowed.");
                break;
        }

        return result;
    }
}
