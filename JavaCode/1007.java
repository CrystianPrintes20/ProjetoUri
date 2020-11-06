import java.io.IOException;
import java.util.Scanner;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
     Scanner ler = new Scanner (System.in);
            int A = ler.nextInt();
            int B = ler.nextInt();
            int C = ler.nextInt();
            int D = ler.nextInt();
            int dif = ((A*B)-(C*D));
                System.out.printf("DIFERENCA = "+ dif);
                System.out.println();
 
    }
 
}