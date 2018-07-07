import unittest

main_set=[]
def get_permutations(string):
    # Generate all permutations of the input string
    global main_set
    main_set=[]
    if len(string) == 0: return set([''])
    string_list = list(string)
    permute(string_list,0,len(string)-1)
    # print (main_set)
    return set(main_set)

def addtoset(string_list):
    string = ''.join(string_list)
    # print (string)
    main_set.append(string)

def permute(string_list,start,end):
    if start == end :
        addtoset(string_list)
    else:
        for i in range (start,end+1):
            string_list[start],string_list[i]=string_list[i],string_list[start]
            permute(string_list,start+1,end)
            string_list[start], string_list[i] = string_list[i], string_list[start]

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)