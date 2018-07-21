import re

from collections import defaultdict


def countOfAtoms(formula):
    stk = []
    parse = list(filter(lambda c: c, re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)))
    count = defaultdict(int)
    i = 0
    while i < len(parse):
        token = parse[i]
        if token == '(':
            stk.append(count)
            stk.append(token)
            count = defaultdict(int)
        elif token == ')':
            tmp = stk.pop()
            while tmp != '(':
                for k, v in tmp.items():
                    count[k] += v
                tmp = stk.pop()
        elif token.isdigit():
            if parse[i - 1] == ')':
                for k, v in count.items():
                    count[k] = v * int(token)
            else:
                count[parse[i - 1]] += int(token) - 1
        else:
            count[token] += 1
        i += 1
    while stk:
        tmp = stk.pop()
        for k, v in tmp.items():
            count[k] += v
    # sorted_count = sorted(count.items(), key=lambda (k, v): k)
    sorted_count = sorted(count.items(), key=lambda x: x[0])
    result = ''
    for k, v in sorted_count:
        result += k
        if v != 1:
            result += str(v)
    return result

print(countOfAtoms('H2O'))
print(countOfAtoms('Mg(OH)2'))
print(countOfAtoms('K4(ON(SO3)2)2'))
print(countOfAtoms('C10H16O'))
print(countOfAtoms('Zn(NO3)2'))
print(countOfAtoms('NaOH'))
print(countOfAtoms('F2'))