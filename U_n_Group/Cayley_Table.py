from tabulate2 import tabulate
from U_n_Group.U_n_Elements import get_all_elements_list

'''
This program prints the cayley table of U(n) group.
'''
def draw_cayley_table(size):
    prime_list = get_all_elements_list(size)  # Getting the list of all elements of the group.

    data = []
    for x in prime_list:
        column = [x]
        for y in prime_list:
            column.append(x * y % size)
        data.append(column)


    headers = ["× mod n"] + prime_list
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


def main():
    n = int(input("Enter the value of n for U(n) group: "))
    draw_cayley_table(n)

if __name__ == "__main__":
    main()