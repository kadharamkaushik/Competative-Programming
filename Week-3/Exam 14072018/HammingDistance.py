def hammingdistance(x,y):
    res = (x^y)
    temp=0
    while(res>0):
        t=res%2
        if t==1:
            temp+=1
        res=res//2
    return temp

print (hammingdistance(25,30))
print (hammingdistance(1,4))
print (hammingdistance(25,30))
print (hammingdistance(100,250))
print (hammingdistance(1,30))
print (hammingdistance(0,255))

