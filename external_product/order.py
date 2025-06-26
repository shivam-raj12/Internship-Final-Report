from math import gcd
from math import lcm
from tabulate2 import tabulate

def find_order(m, n, e1, e2):
    order_of_e1_in_m = m // gcd(e1, m)
    order_of_e2_in_n = n // gcd(e2, n)

    return lcm(order_of_e1_in_m, order_of_e2_in_n)

def main():
    m = int(input("Enter the value of m for Z_m x Z_n group: "))
    n = int(input("Enter the value of n for Z_m x Z_n group: "))

    elements = [[x,y] for x in range(0, m) for y in range(0, n)]

    data = []
    for e in elements:
        order = find_order(m, n, e[0], e[1])
        data.append([f"{e[0]}x{e[1]}", order])

    print(tabulate(data, ["Element", "Order"], tablefmt = "fancy_grid"))

if __name__ == "__main__":
    main()