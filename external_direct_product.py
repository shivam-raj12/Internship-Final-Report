from math import gcd


def Us_elements():
    print("This software lists the elements of U_s(st), where s and t are relatively prime.")

    s = int(input("Value of s: "))
    t = int(input("Value of t: "))
    if gcd(s, t) != 1:
        print("This two number is not relatively prime. Please try again.")
        return
    elements = []

    for x in range(1, s * t):
        if gcd(x, s * t) == 1 and (x - 1) % s == 0:
            elements.append(x)
    print(elements)

def ex2():
    print("This software computes the elements of the subgroup U(n)^k={x^k|x∈U(n)} of U(n) and its order. ")
    n = int(input("Value of n: "))
    k = int(input("Value of k: "))
    elements = set()

    for x in range(1, n):
        if gcd(x, n) == 1:
            elements.add(pow(x, k, n))
    print(sorted(elements))
def main():
    # Us_elements()
    ex2()

if __name__ == "__main__":
    main()
