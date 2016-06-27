# -*- coding: utf-8 -*-
"""
Project Euler

Problem 44: Pentagon numbers

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of
D?


Analysis



"""

def invPent(aPenNo):
    return int(round(1/6 + (1/36+2/3*aPenNo)**0.5,0))
    
def pent(aNumber):
    return int(round((aNumber*(3*aNumber-1)/2),0))


from time import time

if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    testNo = round(5/6, 4)
    maxToTry = int(1e6)
    PentNoList = [0] * maxToTry
    PentNoListDict = {}
    #PentNoDict = {}
    minPent = [0, 0, 5482660 + 1, 0]    #set based on known solution

    for k in range(1, maxToTry):
        pentK = int(k*k*1.5 - 0.5 * k)
        PentNoListDict[pentK] = True
        PentNoList[k] = int(k*k*1.5 - 0.5 * k)
        #PentNoDict[k] = int(k*k*1.5 - 0.5 * k)
    maxPentFound = max(PentNoList)
    print("Initial", maxToTry, "Pentagon numbers found")


    for pentKSeqNo, pentK in enumerate(PentNoList[2:5000]):
        if pentK % 1000 == 0:
            print("pentK:", pentK, flush=True)
        for pentJ in PentNoList[1:pentKSeqNo]:
            pentSum = pentJ + pentK
            if pentSum > PentNoList[-1]:
                print("PentSum", pentSum, "out of seed range")
                break
            if pentSum not in PentNoListDict:
                continue
            pentDiff = pentK - pentJ
            if pentDiff > minPent[2] or (pentSum - pentDiff) % 2 != 0:
                continue
            if pentDiff not in PentNoListDict:
                continue
            print("Next lowest solution found: pentK:", pentK, ", pentJ:",
                  pentJ, ", pentSum:", pentSum, ", pentDiff:", pentDiff,
                  invPent(pentK), invPent(pentJ), invPent(pentSum),
                  invPent(pentDiff), flush=True)
            minPent = [invPent(pentK), invPent(pentJ), invPent(pentDiff),
                       invPent(pentSum)]
        if minPent[2] != 5482661:
            if PentNoList[minPent[2]] == 1:
                break


    totalTime = time() - startTime
    print("\n\nThe value of 'D' is", str(minPent[2])+
          ". [k, j, m, n, Pent[k], Pent[j], Pent[m], Pent[n]]:", minPent,
          PentNoList[minPent[0]], PentNoList[minPent[1]],
          PentNoList[minPent[2]], PentNoList[minPent[3]])
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The value of 'D' is 1912. [k, j, m, n, Pent[k], Pent[j], Pent[m], Pent[n]]:
[2167, 1020, 1912, 2395] 7042750 1560090 5482660 8602840
Time to find: 14.895

"""