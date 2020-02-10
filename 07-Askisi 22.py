#-*- coding: utf-8 -*-

##22. Γράψτε μία συνάρτηση σε python η οποία θα δέχεται ως όρισμα μία λίστα και
##θα ελέγχει αν είναι ταξινομημένη σε αύξουσα σειρά.
##Θα επιστρέφει true αν είναι ταξινομημένη και false σε κάθε άλλη περίπτωση. 


def checkSort(L):
    "έλεγχος ταξινόμησης λίστας σε αύξουσα σειρά."
    N = len(L)
    issorted = False
    i = 0
    while i < N-1 and issorted == False:
        issorted = True
        for j in range(N-1,i,-1):
            if L[j]<L[j-1]:
                issorted = False
        i += 1
    return issorted

L1 = sorted([3,10,4,12,8])
L2 = [3,43,10,11,4,12,19,8]
print L1

print checkSort(L1)
print checkSort(L2)
