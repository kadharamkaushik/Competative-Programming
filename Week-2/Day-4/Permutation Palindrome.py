import unittest


def has_palindrome_permutation(the_string):
    # Check if any permutation of the input is a palindrome
    count=0
    dict={}
    for i in range(0,len(the_string)):
        if (dict.__contains__(the_string[i])):
            dict[the_string[i]]+=1
        else:
            dict[the_string[i]]=1
    count=0
    for key in dict.keys():
        count+=dict[key]%2
        # print (the_string+'----'+count)
        if(count>1):
            return False
    # print(the_string + '----' + str(count))
    return True


# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)