from math import factorial, prod
from collections import Counter
from tabulate2 import tabulate

'''
This program returns the list of possible cycles of the Symmetric group S_n.
'''
def find_unique_additive_lists(n):
    unique = set()
    result = []

    def backtrack(current, total, start):
        if total > n:
            return
        if total <= n and current:
            key = tuple(sorted(current))
            if key not in unique:
                unique.add(key)
                result.append(list(key))
        for i in range(start, n + 1):
            if i >= 2:
                current.append(i)
                backtrack(current, total + i, i)
                current.pop()

    backtrack([], 0, 2)
    return result



'''
Counts the number of cycles in the given permutation of the symmetric group S_n.
'''
def element_counter(n, cycle):
    if len(cycle) == 1:
        order = factorial(n)
        return order // (cycle[0] * factorial(n - cycle[0]))
    else:
        total_sum = sum(cycle)
        numerator = prod([n - i for i in range(total_sum)])
        denominator = prod(cycle)
        denominator = denominator * prod([factorial(y) for y in Counter(cycle).values()])

        return numerator // denominator


def main():
    size = int(input("Enter the size of the set: "))

    data = [["1", 1]]  # Initializing 1 cycle element which is `e` only.

    total_possible_cycles = find_unique_additive_lists(size)

    for cycle in total_possible_cycles:
        data.append(["x".join([str(x) for x in cycle]), element_counter(size, cycle)])

    print(tabulate(data, headers = ["Cycle", "Number of elements"], tablefmt = "fancy_grid"))


if __name__ == '__main__':
    main()
