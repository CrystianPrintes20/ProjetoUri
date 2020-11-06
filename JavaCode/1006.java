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
            double A = ler.nextDouble();
            double B = ler.nextDouble();
            double C = ler.nextDouble();
            double media = ((A*2)+(B*3)+(C*5))/10;
                System.out.printf("MEDIA = %.1f", media);
                System.out.println();
 
    }
 
}