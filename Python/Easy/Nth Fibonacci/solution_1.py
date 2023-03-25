# O(n) Time / O(n) Space
def getNthFib(n):

    fib_lst = [0 , 1]
    counter = 3
    idx = 0

    if n == 2:
        return fib_lst[1]
    if n == 1:
        return fib_lst[0]


    while counter <= n:

        nextFibNumber = fib_lst[idx] + fib_lst[idx + 1]
        
        fib_lst.append(nextFibNumber)
        counter += 1
        idx += 1
    
    return fib_lst.pop()
