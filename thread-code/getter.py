import mythread

threadNum = 2

def getS(T):
    threadGetS = mythread.GetS(T,threadNum)
    S = threadGetS.get()    
    return S

def getP(S):
    P=[]
    name=0
    for i in xrange(len(S)):
        if i==0:
            current_t3=S[i][0]
            name+=1
        elif current_t3!=S[i][0]:
            current_t3=S[i][0]
            name+=1
        P.append((name,S[i][1]))
    return P,name

def getUniqueP(P,SA12):
    threadGetUniP = mythread.GetUniqueP(P,SA12,threadNum)
    P = threadGetUniP.get()
    return P
    
def getS012(T,P):
    threadGetS012 = mythread.GetS012(T,P,threadNum)
    S0,S1,S2 = threadGetS012.get()
    return S0,S1,S2
