from itertools import permutations

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

#for p in permute([[2,6,8], [4,4,4]]):
#   print p
def permutation(lst):
    if len(lst) == 0:
        return[];
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]

        for p in permutation(remLst):
            l.append([m] +p )
    return l

data = list()


with open('test/3') as file: #ewentualnie wczytywanie z konsoli
                             #plik 2 -dwie maszyny, plik 3 -trzy maszyny
    testfile = eval(file.read())
    perm = permutations([testfile])
    data = list(testfile)
    for p in permutation(data):
        print p