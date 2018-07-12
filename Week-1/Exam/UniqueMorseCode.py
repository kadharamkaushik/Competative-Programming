dict={'A' :".-",'B':"-...",'C' :"-.-.",'D':"-..",'E':".",
'F':"..-.",
'G':"--.",
'H':"....",
'I':"..",
'J':".---",
'K':"-.-",
'L':".-..",
'M':"--",
'N':"-.",
'O':"---",
'P':".--.",
'Q':"--.-",
'R':".-.",
'S':"...",
'T':"-",
'U':"..-",
'V':"...-",
'W':".--",
'X':"-..-",
'Y':"-.--",
'Z':"--.."	}

def unique_morse(li_words):
    new_li=[]
    for word in li_words:
        s=''
        word=str.upper(word)
        for i in range(len(word)):
            s+=dict[word[i]]
        new_li.append(s)
    # print(new_li)
    count=0
    d={}
    for i in range (len(new_li)):
        for j in range (i,len(new_li)):
           if(  new_li[i]==new_li[j]):
               if new_li[i] in d:
                   d[new_li[i]]+=1
               else:
                    d[new_li[i]]=1
    return (len(d))

    pass

print (["gin", "zen", "gig", "msg"],unique_morse(["gin", "zen", "gig", "msg"]))
print (["a", "z", "g", "m"],unique_morse(["a", "z", "g", "m"]))
print (["bhi", "vsv", "sgh", "vbi"]  ,unique_morse(["bhi", "vsv", "sgh", "vbi"]  ))
print (["a", "b", "c", "d"]  ,unique_morse(["a", "b", "c", "d"]  ))
print (["hig", "sip", "pot"]  ,unique_morse(["hig", "sip", "pot"]  ))

