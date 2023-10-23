import java.util.Scanner;

public class SimpleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num1, num2,choice, result;
        choice=scanner.nextInt();

        System.out.print("Enter the first number: ");
        num1 = scanner.nextInt();

        System.out.print("Enter the second number: ");
        num2 = scanner.nextInt();

        System.out.print("Enter your choice ");
        System.out.println("\1.add\2.sub\3.mul\4.div");
        choice = scanner.nextInt();

        switch (choice) {
            choice "1":
                result = num1 + num2;
                System.out.println("Result: " + result);
                break;
            choice "2":
                result = num1 - num2;
                System.out.println("Result: " + result);
                break;
            choice "3":
                result = num1 * num2;
                System.out.println("Result: " + result);
                break;
            choice "4":
                if (num2 != 0) {
                    result = num1 / num2;
                    System.out.println("Result: " + result);
                } else {
                    System.out.println("Division by zero is not allowed.");
                }
                break;
            default:
                System.out.println("Invalid option.");
        }
    }
}
