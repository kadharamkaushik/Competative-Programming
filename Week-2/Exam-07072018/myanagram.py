def checkanagram(s,t):
    print (s,t)
    s=str.lower(s)
    t=str.lower(t)
    s=s.replace(" ","")
    t=t.replace(" ","")
    dict1={}
    dict2={}
    if(len(s)==len(t)):
        for i in range(0,len(s)):
            if s[i] in dict1.keys():dict1[s[i]]+=1
            else : dict1[s[i]]=1
            if t[i] in dict2.keys():dict2[t[i]]+=1
            else : dict2[t[i]]=1
        count=0
        # print (dict1)
        # print (dict2)
        for key in dict1.keys():
            if(dict1[key]==dict2[key]):
                # print ('in')
                count+=1
            else:
                # print ('False')
                break
        if(count==len(dict1)):
            print('True')
        else: print('False')
    else:
        print ('False')

checkanagram('anagram','nagaram')
checkanagram('Keep','peek')
checkanagram('Mother In Law','Hitler Woman')
checkanagram('School Master','The Classroom')
checkanagram('ASTRONOMERS','NO MORE STARS')
checkanagram('Toss','Shot')
checkanagram('joy','enjoy')
checkanagram('Debit Card','Bad Credit')
checkanagram('SiLeNt CAT','LisTen AcT')
checkanagram('Dormitory','Dirty Room')





