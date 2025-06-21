from tabulate2 import tabulate

'''
This program prints the inverse and order of each elements of Z_n group.
'''
def print_all_elements_inverse_and_order(size):
    element_list = [i for i in range(0, size)] # All the elements of Zn group

    data = []
    for x in element_list:
        column = [x, size - x]

        # Calculating the order of group
        for i in range(1, size + 1):
            if (i * x) % size == 0:
                column.append(i)
                break
        data.append(column)

    headers = ["Element", "Inverse", "Order"]
    print(tabulate(data, headers = headers, tablefmt = "fancy_grid"))

def main():
    n = int(input("Enter the value of n for Zₙ group: "))
    print_all_elements_inverse_and_order(n)

if __name__ == '__main__':
    main()