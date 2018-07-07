main_set=[]
def get_permutations(string):
    # Generate all permutations of the input string
    if len(string) == 0: return set([''])
    string_list = list(string)
    permute(string_list,0,len(string)-1)
    return main_set

def addtoset(string_list):
    string = ''.join(string_list)
    print (string)
    main_set.append(string)

def permute(string_list,start,end):
    if start == end :
        addtoset(string_list)
    else:
        for i in range (start,end+1):
            string_list[start],string_list[i]=string_list[i],string_list[start]
            permute(string_list,start+1,end)
            string_list[start], string_list[i] = string_list[i], string_list[start]

print (set(get_permutations('ab')))