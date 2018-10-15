
'''

Beispielprogramm in Python

    Bestimmen des ggT von zwei eingegebenen
    Zahlen mit dem Euklidschen Algorithmus

'''


# Einlesen der 1. Zahl
x = int(input("1. Zahl: "))

# Einlesen der 2. Zahl
y = int(input("2. Zahl: "))

# Euklidscher Algorithmus zur Bestimmung des ggT
while x > 0:
    if x < y:
        h = x
        x = y
        y = h
    x = x - y

# Ausgeben des Ergebnisses
print(" ---> ggt = ",  str(y))
