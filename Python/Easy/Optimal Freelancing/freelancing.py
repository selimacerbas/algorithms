jobs = [
    {'deadline': 1, 'payment':1},
    {'deadline': 5, 'payment':4},
    {'deadline': 1, 'payment':2},
    {'deadline': 3, 'payment':3},
    {'deadline': 6, 'payment':7}
]

# job - deadline -> After deadline no value to complete the job
# Write a function that returns maximum profit can be obtained in 7 days.
# Each job takes 1 full day. And deadline 1 has priority.

# O(n* log(n) time | O(1) space)
def optimalFreelancing(jobs):
    LENGTH_OF_WEEK = 7
    profit = 0
    jobs.sort(key=lambda job: job['payment'], reverse=True) # We need to specifically sort it by the payment value.
    timeline = [False] * LENGTH_OF_WEEK # This creates a List that has 7 False value. Each False value means that we can take job to that.

    for job in jobs:
        maxTime = min(job['deadline'], LENGTH_OF_WEEK) # First we need to find the possible latest deadline of the job. If deadline is more than 7 than we take 7.
        for time in reversed(range(maxTime)):
            if timeline[time] is False:
                timeline[time] = True
                profit += job['payment']
                break
    return profit

if __name__ == "__main__":
    print(optimalFreelancing(jobs))