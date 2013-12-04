import sys

def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1)+fibo(n-2)


def memoize(f):
   cache = {}
   def memf(*x):
       if x not in cache:
           cache[x] = f(*x)
       return cache[x]
   return memf


@memoize
def fibo_memoized(n):
    if n < 3:
        return 1
    return fibo_memoized(n-1)+fibo_memoized(n-2)


def fibo_loop(n):
    a, b = 0, 1
    for count in xrange(n):
        a, b = b, a+b
    return a


fns = { "fibo" : fibo,
        "fibo_memoized": fibo_memoized,
        "fibo_loop": fibo_loop,
}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: %s <function> <n>"
        exit()

    fn = sys.argv[1]

    if fn not in fns:
        print "The function %s is not in %s" % (fn, fns.keys())
        exit()

    n = int(sys.argv[2])

    if n < 1:
        print "n must be >= 1"
        exit()

    f = fns[fn]
    print f(n)
