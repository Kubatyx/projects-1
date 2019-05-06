import time


# 2 algorytmy O(n^2) oraz sprawdzenie czasu wykonywania 





def schrage(N):
    Cmax = 0 
    o = [] 
    NN = N[:] 
    NG = [] 
    t = 0 
    rj = NN.index(min(NN, key=lambda elem: elem[0]))
    # przeszukiwanie listy i zwracanie najmnieszego indexu elem 
    # z czasu przygotowania rj
    
    while (len(NN) != 0 or len(NG) != 0): 
        while (len(NN) != 0 and  NN[rj][0] <= t): 
            j = NN.pop(rj) # remove
            NG.append(j)
            if len(NN) != 0: rj = NN.index(min(NN, key=lambda elem: elem[0]))
        if len(NG) == 0: t = NN[rj][0]
        else:
            qj = NG.index(max(NG, key=lambda elem: elem[2])) 
            jj = NG.pop(qj) # remove max qj from NG
            o.append(jj)
            pj = jj[1] 
            t = t + pj
            qjj = jj[2]
            Cmax = max(Cmax, t + qjj)
    return o, Cmax

def schrage_pmtn(N):
    Cmax = 0
    NN = N[:]
    NG = [] 
    o = []
    t = 0
    r0 = 0
    p0 = 0
    q0 = float('inf') # nieskonczonsc
    l = [r0, p0, q0] # biezace zadanie
    rj = NN.index(min(NN, key=lambda elem: elem[0]))

    while (len(NN) != 0 or len(NG) != 0): 
        while (len(NN) != 0 and NN[rj][0] <= t):
            j = NN.pop(rj) # usuniecie najmniejszego czasu przygotowania
            NG.append(j)

            if (len(NN) != 0): rj = NN.index(min(NN, key=lambda elem: elem[0]))

            if j[2] > l[2]:  # czasy przerwan qj > ql
                l[1] = t - j[0] # pj = t - rj
                t = j[0] # t = rj
                if l[1] > 0: # pj > 0 
                    NG.append(l)  # przerwany
        if len(NG) == 0: 
            t = NN[rj][0] # wartosc rj
        else:
            qj = NG.index(max(NG, key=lambda elem: elem[2]))
            jj = NG.pop(qj) 
            l = jj # l = j
            t = t + jj[1] # t = t + pj
            Cmax = max(Cmax, t + jj[2])
            o.append(jj) 
    return o, Cmax


# czytanie z pliku

tab = []
def file(filename):
    with open(filename, "r") as file:
        jobs = [int(x) for x in next(file).split()]  
        for line in file:
            tab.append([int(x) for x in line.split()])
        o = [list(x) for x in tab]
    return o



plik3 = ["dane_testowe_RPQ/in50.txt", "dane_testowe_RPQ/in100.txt", "dane_testowe_RPQ/in200.txt"]


plik = file("dane_testowe_RPQ/in50.txt") # 50 100 200
tic1 = time.clock()
O, Cmax = schrage(plik)
print("Wynik Cmax", Cmax)
toc1 = time.clock()
t1=toc1 - tic1
print "Schrage time process:", round(toc1 - tic1/100,5),"seconds\n"

tic2 = time.clock()
O, Cmax = schrage_pmtn(plik)
print("Wynik Cmax", Cmax)
toc2 = time.clock()
t2=toc2 - tic2
print "Schrage_pmtn time process:", round(toc2 - tic2/100,5),"seconds\n"

print "Roznica miedzy Schrage_ptmn a Schrage:",t2-t1,"seconds"
