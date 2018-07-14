def trap_fn(ls):
    n=len(ls)
    arr_l=[0]*n
    arr_r=[0]*n
    arr_l[0]=ls[0]
    for i in range(1,n):
        arr_l[i]=max(arr_l[i-1],ls[i])
    arr_r[n-1]=ls[n-1]
    for i in range(n-2,-1,-1):
        arr_r[i]=max(arr_r[i+1],ls[i])
    water=0
    for i in range(0,n):
        water+=min(arr_l[i],arr_r[i])-ls[i]
    return water



    pass

print (trap_fn([0, 1, 0, 2, 1, 0, 1]))
print(trap_fn([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap_fn([0, 1, 0, 2, 1, 0, 5, 1, 0, 2]))
print(trap_fn([0, 1, 0, 5, 1, 0, 2]))
print(trap_fn([0, 5, 1, 3, 4, 0, 1]))