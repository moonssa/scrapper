from indeed import get_jobs as get_indeed_jobs


indeed_jobs = get_indeed_jobs()
for num, job in enumerate(indeed_jobs):
    print(num, job, sep="-")