#!/usr/bin/python
# -*- coding: latin-1 -*-


def ggt_subtraktion(zahlA, zahlB):

    """
    Berechnet den grössten gemeinsamen Teiler zweier Zahlen.
    Dazu wird die kleinere der beiden Zahlen von der grösseren
    Subtrahiert, bis die beiden Zahlen gleich sind.

    Return GGT wenn input OK, sonst -1.
    """

    try:
        zahlA = int(zahlA)
        zahlB = int(zahlB)
        while (zahlA != zahlB):
            if (zahlA > zahlB):
                zahlA = zahlA - zahlB
            else:
                zahlB = zahlB - zahlA
        return zahlA
    except ValueError:
        return -1


#
# Testfälle
#
a, b = 12, 9
print("GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b))

a, b = 36, 8
print("GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b))

a, b = 32, "A"
print("GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b))

a, b = 36, 12
print("GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b))

a, b = 7, 11
print("GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b))

a, b = 7, -11
print("GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b))
