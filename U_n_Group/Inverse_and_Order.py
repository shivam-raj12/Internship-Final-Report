from math import gcd
from tabulate2 import tabulate

from U_n_Group.U_n_Elements import get_all_elements_list

'''
This program prints the inverse and order of all the elements of U(n) group.
'''
def print_all_elements_inverse_and_order(size):
    prime_list = get_all_elements_list(size)   # Getting the list of all elements of U(n) group.

    data = []  # Stores the list of all elements with their inverses and orders.
    for x in prime_list:
        column = [x]  # A single element list to store its inverse and order.


        # Here it calculates the inverse of the element
        for inverse in prime_list:
            if (x * inverse) % size == 1:
                column.append(inverse)
                break

        # Here it calculates the order of the element
        for order in range(1, size + 1):
            if pow(x, order, size) == 1:
                column.append(order)
                break
        data.append(column)

    # Printing the calculated element's inverse and order with the help of tabulate library
    headers = ["Element", "Inverse", "Order"]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def main():
    n = int(input("Enter the value of n for U(n) group: "))
    print_all_elements_inverse_and_order(n)

if __name__ == '__main__':
    main()