def primes(int kmax):
    cdef int n, k, i
    cdef int p[100000]
    if kmax > 100000:
        kmax = 100000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
        n = n + 1
    return [p[i] for i in range(kmax)]
