def johnson(times):
    job_count = len(times)
    job_ids = list(range(1, job_count+1))
    
    l1 = []
    l2 = []
    for job_info in sorted(zip(job_ids, times), key=lambda x: min(x[1])):
        job_id = job_info[0]
        job_times = job_info[1]
        if job_times[0] < job_times[1]:
            l1.append(job_id)
        else:
            l2.insert(0, job_id)
    
    return l1 + l2