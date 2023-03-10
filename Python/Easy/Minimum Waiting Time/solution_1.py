
lst = [3, 2, 1, 2, 6]


def minimumWaitingTime(queries):

    hash_tbl = {}
    queries.sort()
    sums = 0

    for i in range(len(queries) - 1):
        first = queries[i]
        second = queries[i + 1]
        sums += first

        hash_tbl[sums] = second
        
    
    return sum(hash_tbl.keys())

print(minimumWaitingTime(lst))
