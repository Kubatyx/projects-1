from makespan import makespan
from time import time
from optimal import opt
from johnson import johnson
 
def test(file, testcase):
    start = time()
    result = makespan(file(testfile), testfile)
    end = time()

    print "Best Makespan =", result
    return (result, end - start)

with open('test/2') as file: #ewentualnie wczytywanie z konsoli
    testfile = eval(file.read())
    print "### Optymalne: "
    spr = test(opt, testfile)
    print "### Johnson:"
    spr = test(johnson, testfile)
