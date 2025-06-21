from collections import defaultdict
from tabulate2 import tabulate

'''
This program prints all the cyclic subgroups of U(n) group.
'''
def print_cyclic_subgroups(size):
    int_list = [i for i in range(0, size)]

    subgroups = defaultdict(list)
    for element in int_list:
        subgroup_generated_by_element = set()
        for x in range(0, size + 1):
            subgroup_generated_by_element.add(element * x % size)
        subgroups[frozenset(subgroup_generated_by_element)].append(element)


    # Prints the generated subgroups by each elements of the U(n) group.
    headers = ["Elements", "Group Generated"]
    data = []
    for key, value in subgroups.items():
        data.append([", ".join(map(str, sorted(value))), sorted(list(key))])
    print(tabulate(data, headers = headers, tablefmt = "fancy_grid"))

    # Prints the total number of cyclic subgroups of Zn group.
    total_data = [["Total subgroups", f"{len(subgroups)} (Including trivial subgroups)"]]
    print(tabulate(total_data, tablefmt = "simple_grid"))

def main():
    n = int(input("Enter the value of n for Zₙ group: "))
    print_cyclic_subgroups(n)

if __name__ == '__main__':
    main()