#-*- coding: utf-8 -*-

##11. Να γράψετε μία συνάρτηση σε python η οποία θα παίρνει ως ορίσματα
##μία λίστα και έναν αριθμό και θα επιστρέφει μια λίστα με τις θέσεις
##στις οποίες θα εμφανίζεται αυτός ο αριθμός στη αρχική λίστα.  
    

import random

def findNum(L,num):
    POS = []
    pos = -1
    for i in range(len(L)):
        if L[i] == num:
            pos = i
            POS.append(pos)
    return POS


A = [4, 5, 79, 5, 99, 44, 5, 89]

print findNum(A,5)
