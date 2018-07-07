import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    # Shuffle the input in place
    if len(the_list) <= 1:
        return the_list

    l = len(the_list) - 1

    for x in range(0, l):
        rand = get_random(x, l)
        if rand != x:
            the_list[x], the_list[rand] = the_list[rand], the_list[x]


sample_list = [1, 2, 3, 4, 5]
print
'Sample list:', sample_list

print
'Shuffling sample list...'
shuffle(sample_list)
print (sample_list)