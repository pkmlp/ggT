#!/usr/bin/python
# -*- coding: latin-1 -*-


def ggt_subtraktion(zahlA, zahlB):
    
    """
    Berechnet von zwei übergegebenen Zahlen den grössten gemeinsamen Teiler.
    Dazu wird immer die kleinere der beiden Zahlen von dergrössere Subtrahiert,
    bis die beiden Zahlen gleich sind. 
    """

    while (zahlA != zahlB):
        if (zahlA > zahlB):
            zahlA = zahlA - zahlB
        else:
            zahlB = zahlB - zahlA
    return zahlA




#
# Testfälle
#
a, b = 12, 9
print "GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b)

a, b = 36, 8
print "GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b)

a, b = 32, 24
print "GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b)

a, b = 36, 12
print "GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b)

a, b = 7, 11
print "GGT von:", a, "und", b, "ist:", ggt_subtraktion(a, b)
