from collections import defaultdict
from tabulate2 import tabulate
from U_n_Group.U_n_Elements import get_all_elements_list

'''
This program prints all the cyclic subgroups of U(n) group.
'''
def print_cyclic_subgroups(size):
    coprime_list = get_all_elements_list(size) # Getting the list of all elements

    order_of_group = len(coprime_list) # Calculating the order of the group

    subgroups = defaultdict(list)
    for element in coprime_list:
        subgroup_generated_by_element = set() # Stores the subgroup generated by each element
        for x in range(0, order_of_group + 1):
            el = pow(element, x, size)
            subgroup_generated_by_element.add(el)
            if el == 1 and x != 0:
                break
        subgroups[frozenset(subgroup_generated_by_element)].append(element)

    # Prints the generated subgroups by each elements of the U(n) group.
    headers = ["Elements", "Subgroup Generated"]
    data = []
    for key, value in subgroups.items():
        data.append([", ".join(map(str, sorted(value))), sorted(list(key))])
    print(tabulate(data, headers = headers, tablefmt = "fancy_grid"))

    # Prints the total number of cyclic subgroups of U(n) group.
    total_data = [["Total subgroups", f"{len(subgroups)} (Including trivial subgroups)"]]
    print(tabulate(total_data, tablefmt = "simple_grid"))

def main():
    n = int(input("Enter the value of n for U(n) group: "))

    print_cyclic_subgroups(size = n)

if __name__ == "__main__":
    main()
