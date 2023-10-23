// **Task 4:** String Reversal Script in Java
// - Write a Java script to reverse strings.

import java.util.Scanner;

public class Stringrev{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a string");
        String str=sc.nextLine();
        for(int i=str.length()-1;i>=0;i--)
        System.out.print(str.charAt(i));

    }
}