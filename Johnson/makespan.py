import sys

def makespan(perm, times):
    job_count = len(perm)
    machine_count = len(times[0])
    makespan = [[0] * (machine_count +1) for i in range(0, job_count +1)]
    for i, job in enumerate(perm):
        for machine in range(0, machine_count):
            z = makespan[i + 1][machine + 1] = max(makespan[i][machine + 1], makespan[i + 1][machine]) + times[job - 1][machine]          
    for i in range(0,len(times)):
		sys.stdout.write("       Machine: " + str(i+1)+"    ")
    print "\nTimes:", makespan[1:]
    print "Makespan = ", z, "\n"
    return makespan[job_count][machine_count]


 
