#!/usr/bin/env python
import sys
import getter
import merger
from operator import itemgetter
import re
import time
import radixSort
import gc

def dna2int(dna):
   if   dna =='a' or dna=='A': return 1   
   elif dna =='c' or dna=='C': return 2
   elif dna =='g' or dna=='G': return 3
   elif dna =='n' or dna=='N': return 4
   elif dna =='t' or dna=='T': return 5

def dnaFormat(dna):
    # capitalize dna
    dna = dna.upper()
    # delete all characters beyond number and letter
    dna_re = re.compile('\W')
    dna = dna_re.sub('',dna)
    # "dna"=>[d,n,a]
    dna = [dna2int(t) for t in dna]
    return dna

# parallel DC3
def pDC3(T,append_len):
    # [m,i,s,s,i,s,s,i,p,p,i,0,0,0],in case [i,0,0] is missed
    t3=time.time()
    for i in xrange(append_len): T.append(0)
    # algo<line 1> S:[([i,s,s],1),...,([i,0,0],10),([0,0,0],11),([0],13)]
    S = getter.getS(T)
    t4=time.time()
    print t4-t3
    # algo<line 2> sort S by item(0), S:[([0],13),([0,0,0],11),...,([s,s,i],5)]
    S=sorted(S, key=itemgetter(0))

    P,max_name = getter.getP(S)
    # algo<line 4> if names in P are not unique
    if max_name <len(P):
        # algo<line 5> sort P (1,4,7,...,2,5,8),P:[(5,1),(5,4),...,(6,8),(2,11)]
        P=sorted(P, key=lambda p: (p[1]%3,p[1]/3))
        # algo<line 6> recursively compute pDC3([5,5,4,3,1,7,7,6,2])
        SA12 = pDC3([pair[0] for pair in P],append_len)

        P = getter.getUniqueP(P,SA12)
 
    P = radixSort.sort(P, 1)

    S0,S1,S2 = getter.getS012(T,P)
    
    SA=merger.merge(S0,S1,S2)
    # pop appendix [11,10,7,4,...] => [10,7,4,...]
    while(len(SA)>(len(T)-append_len)):SA.pop(0)
    return SA                

if __name__ == "__main__":
    # the number of zeros append in the end of dna
    append_len = 3
    # get dna string
    dna = sys.stdin.readline()
    # format dna
    dna = dnaFormat(dna)
    t1=time.time()
    # get suffix array by pDC3 algo
    SA = pDC3(dna,append_len)
    t2=time.time()
    # output
    print SA
    print t2-t1
    # in case threadpool throw interpreter shutdown warning
    sys.stdout.close()
