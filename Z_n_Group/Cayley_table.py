from tabulate2 import tabulate

'''
This program prints the cayley table of Zn group.
'''
def draw_cayley_table(size):
    int_list = [i for i in range(0, size)]
    headers = ["+ mod n"] + int_list
    data = list()
    for x in int_list:
        column = list()
        column.append(x)
        for y in int_list:
            column.append((x + y) % size)
        data.append(column)

    print(tabulate(data, headers = headers, tablefmt = "fancy_grid"))

def main():
    n = int(input("Enter the value of n for Zₙ group: "))
    draw_cayley_table(n)

if __name__ == '__main__':
    main()