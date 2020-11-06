import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
    Scanner ler = new Scanner (System.in);
     int A;
     int B;
     int X;
        A = ler.nextInt();
        B = ler.nextInt();
        X = (A + B);
        System.out.println("X = "+X);
    }
 
}