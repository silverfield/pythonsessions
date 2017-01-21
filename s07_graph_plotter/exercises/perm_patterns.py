__author__ = 'ferrard'


def is_pattern(sub_perm, pattern):
    if len(sub_perm) != len(pattern):
        return False
    sub_perm_sorted = [sub_perm[i] for i in range(len(sub_perm))]
    sub_perm_sorted.sort()
    ranks = {}
    for i in range(len(sub_perm_sorted)):
        ranks[sub_perm_sorted[i]] = i
    sub_perm_pattern = [ranks[x] + 1 for x in sub_perm]

    return all(sub_perm_pattern[i] == pattern[i] for i in range(len(pattern)))


def has_pattern(perm, pattern):
    for i in range(len(perm)):
        if is_pattern(perm[i:i + len(pattern)], pattern):
            print("Found pattern at " + str(i) + ": " + str(perm[i:i + len(pattern)]))
            return True
    return False


def main():
    perm = [5, 4, 1, 6, 7, 2, 3]
    pat_found = [3, 1, 2]
    pat_not_found = [4, 3, 2, 1]

    print(has_pattern(perm, pat_found))
    print(has_pattern(perm, pat_not_found))


if __name__ == '__main__':
    main()