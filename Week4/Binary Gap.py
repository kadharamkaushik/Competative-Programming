def BinaryGap(n):
    # a=int(input())
    a=bin(n)
    d = 1
    mi = 0
    fl = 0
    if (n > 0):
        a = a[2:]
    else:
        a = a[3:]
    for i in a:
        if (int(i) == 1):
            fl += 1
            if (d > mi):
                mi = d
            d = 1
        else:
            d += 1
    if (fl >= 2):
        return mi
    else:
        return 0
print(BinaryGap(0))
print(BinaryGap(55))
print(BinaryGap(-5))
print(BinaryGap(12354))
print(BinaryGap(6))
print(BinaryGap(256))


