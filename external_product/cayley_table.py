from tabulate2 import tabulate


'''
This program prints the cayley table of Z_m x Z_n group.
'''
def cayley_table(m, n):
    elements = [[x, y] for x in range(0, m) for y in range(0, n)]

    data = []
    header = [" "]
    for e1 in elements:
        column = ["x".join([str(x) for x in e1])]
        header.append("x".join([str(x) for x in e1]))
        for e2 in elements:
            column.append("x".join([str((e1[0] + e2[0]) % m), str((e1[1] + e2[1]) % n)]))
        data.append(column)

    print(tabulate(data, header, tablefmt = "fancy_grid"))

def main():
    m = int(input("Enter the value of m for Z_m x Z_n group: "))
    n = int(input("Enter the value of n for Z_m x Z_n group: "))

    cayley_table(m, n)

if __name__ == "__main__":
    main()
