def m(a, b):
    c = [0] * (len(a) + len(b))
    i=n=k = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i+=1
            n+=1
        else:
            c[n]= b[k]
            k+=1
            n+=1
    while i<len(a):
        c[n]=a[i]
        i+=1
        n+=1
    while k<len(b):
        c[n]=b[k]
        k+=1
        n+=1
    return c


def merge(r):
    a = r[:]
    if len(a) <= 1:
        return
    middle = len(a) // 2
    l = [a[i] for i in range(middle)]
    r = [a[i] for i in range(middle, len(a))]
    merge(l)
    merge(r)
    res = m(l, r)
    return res

f = [8, 11, -6, 3, 0, 1, 1]
print(merge(f))
