
// *Task 1:** Implement a Simple Calculator in Java
//   - Create a basic calculator program in Java.

import java.util.Scanner;

public class calculator {
    public static void main(String args[]){
        int num1,num2,result,choice;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the operation to be performed\n");
        System.out.println("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division");
        choice=sc.nextInt();

        System.out.println("Enter the two numbers ");
        num1=sc.nextInt();
        num2=sc.nextInt();

        switch(choice){
            case 1:result=num1+num2;
            System.out.println("The result is "+result);
            break;
            case 2:result=num1-num2;
            System.out.println("The result is "+result);
            break;
            case 3:result=num1*num2;
            System.out.println("The result is "+result);
            break;
            case 4:
            if(num2==0)
            System.exit(0);
            result=num1/num2;
            System.out.println("The result is "+result);
            break;
            default:System.out.println("wrong choice");
        }
        
    }
    
}
