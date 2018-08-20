
/*

Beispielprogramm in C

    Bestimmen des ggT von zwei eingegebenen Zahlen mit dem Euklidschen Algorithmus

*/



/* Importieren der stdio-Library, die die Funktionen printf() und scanf() enthaelt */
#include <stdio.h>


int main (void) {

    /* Definitionen der benoetigten Variablen */    
    int x, y, h;

    /* Einlesen der 1. Zahl*/
    printf("1. Zahl: ");
    scanf("%d", &x);

    /* Einlesen der 2. Zahl*/
    printf("2. Zahl: ");
    scanf("%d", &y);

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
    printf(" --> ggt = %d\n",y);
    return(0);

}

