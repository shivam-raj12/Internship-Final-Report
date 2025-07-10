from math import gcd

'''
This software computes the elements of the subgroup U(n)^k = {x^k | x in U(n)} of U(n) and its order.
'''
def program2():
    n = int(input("Value of n: "))
    k = int(input("Value of k: "))
    elements = set()

    for x in range(1, n):
        if gcd(x, n) == 1:
            elements.add(pow(x, k, n))
    print(sorted(elements))
    print(f"Order: {len(elements)}")


def main():
    program2()


if __name__ == "__main__":
    main()
