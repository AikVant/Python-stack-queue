#-*- coding: utf-8 -*-

##16. Γράψτε μία συνάρτηση σε python η οποία θα δέχεται ως όρισμα δύο λίστες
##και θα ελέγχει αν όλα τα στοιχεία της πρώτης υπάρχουν και στη δεύτερη
##οπότε θα επιστρέφει True αλλιώς False.   

import random

def commonElements(L1, L2):
    "Αν τα στοιχεία της πρώτης λίστας υπάρχουν στη δεύτερη επιστρέφει True"
    for item in L1:
        if item in L2:
            return True
        else:
            return False

##A = random.sample(xrange(100), 5)
##B = random.sample(xrange(100), 5)
##
##print A
##print B

A = [39, 44, 52, 14, 58]
B = [45, 21, 39, 44, 52, 14, 58, 8, 27, 51]

print commonElements(A,B)
