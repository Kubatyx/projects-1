from itertools import permutations
from makespan import makespan
from johnson import johnson

def opt(times):
    job_count = len(times)

    print "Machine times: \n", times, '\n'
    z = min(permutations(range(job_count)), key = lambda x: makespan(x, times))
    return z