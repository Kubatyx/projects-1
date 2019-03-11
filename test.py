from makespan import makespan
from time import time
from optimal import opt
from johnson import johnson
from itertools import permutations
import numpy as np
import csv 


def test(file, testcase):

    start = time()
    result = makespan(file(testfile), testfile)
    end = time()

    print "Best Makespan =", result
    return (result, end - start)

with open('test/mikrotest') as file: #ewentualnie wczytywanie z konsoli
							 #plik 2 -dwie maszyny, plik 3 -trzy maszyny
    testfile = eval(file.read())
    print "*Przeglad zupelny* \n"
    table= np.loadtxt(file)
    spr = test(opt, testfile)

    spr = test(johnson, testfile)
