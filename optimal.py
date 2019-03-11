from __future__ import print_function
import sys
from itertools import permutations
from makespan import makespan
from johnson import johnson


def opt(times):

    job_count = len(times)
    x = len(times[0])
    print ("Machines times:", times,'\n')
    print ("Amount of machines:", job_count,'\n')

    for k in range(1,x+1):
		print("|Task:",k ,end="|",)
		#sys.stdout.write('Zadanie'+str(k)+'\n')
    for i in range(job_count):
    	print()
    	for j in range(len(times[i])):
			print('|',times[i][j],'s   |', end='')
	
    print ('\n')
    z = min(permutations(range(job_count)), key = lambda x: makespan(x, times))
    return z


