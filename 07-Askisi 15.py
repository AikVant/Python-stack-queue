#-*- coding: utf-8 -*-

##15. Δρ/τα  10 Τετρ.Α. σελ.85 Να γράψετε ένα πρόγραµµα
##το οποίο θα διαβάζει δύο λίστες του ίδιου µεγέθους
##και θα δηµιουργεί µια τρίτη. Σε αυτήν κάθε στοιχείο
##είναι ο µέσος όρος των αντίστοιχων στοιχείων των δύο λιστών,
##δηλαδή των στοιχείων που βρίσκονται στις ίδιες θέσεις.
##Για την εισαγωγή των λιστών και τον υπολογισµό
##της τρίτης λίστας να υλοποιήσετε κατάλληλες συναρτήσεις.

import random

def Eisagogi(n):
    "Συνάρτηση που εισάγει τυχαία στοιχεία σε μία λίστα με n αριθμούς"
    L = []
    for i in range(n):
        x = random.randint(1,100)
        L.append(x)
    return L

def moTwo(A,B):
    "Συνάρτηση που φτιάχνει λίστα με mo στοιχείων σε παράλληλες λίστες"
    M = []
    for i in range(len(A)):
        summ = 0
        for j in range(len(A)):
            summ = A[i] + B[i]
        mo = summ/2.0
        M.append(mo)
    return M

L1 = Eisagogi(5)
L2 = Eisagogi(5)
M = moTwo(L1,L2)


print L1
print L2
print M
        


    