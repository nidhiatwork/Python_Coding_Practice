'''We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
'''

from collections import Counter
def maxProfitAssignment(difficulty, profit, worker):
    jobs = zip(difficulty,profit)
    jobs = sorted(jobs)
    ans,i,best=0,0,0
    worker.sort()
    for skill in worker:
        while i<len(jobs) and skill>=jobs[i][0]:
            best = max(best, jobs[i][1])
            i+=1
        ans+=best
    return ans

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
print(maxProfitAssignment(difficulty, profit, worker))