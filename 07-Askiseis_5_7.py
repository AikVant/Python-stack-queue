#-*- coding: utf-8 -*-

##Συνάρτηση που υπολογίζει το min και επιστρέφει το πλήθος του min
def timesMin(L):
    "Συνάρτηση που υπολογίζει το min και επιστρέφει το πλήθος του min"
    minim = L[0]
    pl = 0
    for item in L:
        if item < minim:
            minim = item
    for item in L:
        if item == minim:
            pl += 1
    return pl

##Συνάρτηση που επιστρέφει το min
def Min(L):
    "Συνάρτηση που επιστρέφει το min"
    minim = L[0]
    for item in L:
        if item < minim:
            minim = item
    return minim

##Συνάρτηση που καλεί την Min(L) και επιστρέφει το πλήθος του min
def timesMin2(L):
    "Συνάρτηση που καλεί την Min(L) και επιστρέφει το πλήθος του min"
    minim = Min(L)
    pl = 0
    for item in L:
        if item == minim:
            pl += 1
    return pl


A = [80, 80, 80, 5, 3, 3, 7, 8, 3, 4, 3, 9, 3]

print timesMin(A)
print timesMin2(A)
    
print timesMin.__doc__
print Min.__doc__
print timesMin2.__doc__

