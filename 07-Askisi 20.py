#-*- coding: utf-8 -*-

##21. Γράψτε μία συνάρτηση σε python η οποία θα δέχεται ως ορίσματα δύο λίστες
##και θα επιστρέφει μία νέα λίστα η οποία θα περιέχει μόνο τα κοινά στοιχεία
##των δύο μόνο. Παράδειγμα αν η πρώτη λίστα είναι η [11, 2,13,10]
##και η δεύτερη η [12, 13, 8,11,51] θα πρέπει να επιστραφεί η λίστα [11,13]. 

def listCommons(A,B):
    "κοινά στοιχεία από δύο λίστες σε μία"
    K = []
    for n1 in A:
        for n2 in B:
            if n1 == n2 and n1 not in K:
                K.append(n1)
    return K

L1 = [3,10,1,4,2,12,8,9]
L2 = [3,43,10,11,4,12,19,8]

print listCommons(L1,L2)
