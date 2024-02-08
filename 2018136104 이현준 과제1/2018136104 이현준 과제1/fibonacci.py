import time

def fib(n) :
    if n == 0 : return 0
    elif n ==1 : return 1
    else :
        return fib(n-1) + fib(n-2)

def fib_iter(n) : 
    if (n < 2) : return n
    
    last = 0
    current = 1
    for i in range(2, n+1) :
        tmp = current
        current += last
        last = tmp
    return current


print('Fibonacci순환(5) :', fib(5))
print('Fibonacci반복(10) :', fib_iter(10))

for i in range(1,40) : 
    t1 = time.time()
    fib_iter(i)
    t2 = time.time()
    fib(i)
    t3 = time.time()
    print("n =", i, "\t반복: ", t2-t1, "순환: ", t3-t2)