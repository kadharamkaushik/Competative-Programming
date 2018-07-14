global res_ls
def findcombinations(ls, position, n, open_br, close):
    # print (ls,position,n,open_br,close)
    if close==n:
        s=''
        for i in range(len(ls)):
            s+=ls[i]
        res_ls.append(s)
        # print("--")
        return
    else:
        if open_br > close :
            ls[position]='}'
            findcombinations(ls,position+1,n,open_br,close+1)
        if open_br <n:
            ls[position]='{'
            findcombinations(ls,position+1,n,open_br+1,close)


def parenthisis(n):
    global res_ls
    res_ls=[]
    parenthesis_ls=[None]*(2*n)
    findcombinations(parenthesis_ls,0,n,0,0)
    print (res_ls,len(res_ls))
    pass

parenthisis(2)
parenthisis(3)
parenthisis(5)
parenthisis(4)
parenthisis(1)
parenthisis(6)
