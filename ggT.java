
/*

Beispielprogramm in Java

    Bestimmen des ggT von zwei eingegebenen Zahlen mit dem Euklidschen Algorithmus

*/



// importieren der util-Klasse, die den Scanner enthaelt
import java.util.*;


public class ggT {

    public static void main(String args[]) {

        /* Definitionen der benoetigten Variablen */    
        int x,y,h;
        Scanner sc = new Scanner(System.in);

        /* Einlesen der 1. Zahl*/
        System.out.print("1. Zahl: ");
        x = sc.nextInt();

        /* Einlesen der 2. Zahl*/
        System.out.print("2. Zahl: ");
        y = sc.nextInt();

        /* Euklidscher Algorithmus zur Bestimmung des ggT */
        while (x > 0) {
            if (x < y) {
                h = x;
                x = y;
                y = h;
            }
            x = x - y;
        }

        /* Ausgeben des Ergebnisses */
        System.out.println(" ---> ggt = " + y);
        sc.close();

    }

}


