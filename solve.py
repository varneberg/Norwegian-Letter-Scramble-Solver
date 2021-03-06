import random
from itertools import permutations


def shuffle(s):
    perms = [''.join(p) for p in permutations(s)]
    perms = set(perms)
    return perms


def sort_list(word):
    list = []
    with open("big_no_wordlist.txt", 'r') as f:
        for line in f:
            line = line.strip().lower()
            if len(word) == len(line):
                list.append(line)
    list.sort()
    sorted_set = set(list)
    return sorted_set


def solve(s):
    sorted_list = sort_list(s)
    new_word = shuffle(s)
    return new_word.intersection(sorted_list)


if __name__ == '__main__':
    s = input("Hvilke bokstaver er opgitt?\n").lower()
    answers = solve(s)
    for x in answers:
        print("{}".format(x))