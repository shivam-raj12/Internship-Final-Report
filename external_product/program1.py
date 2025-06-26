from math import gcd


def program1():
    s = int(input("Value of s: "))
    t = int(input("Value of t: "))
    if gcd(s, t) != 1:
        print("This two number is not relatively prime. Please try again.")
        return
    elements = []

    for x in range(1, s * t):
        if gcd(x, s * t) == 1 and x % s == 1:
            elements.append(x)
    print(elements)

def main():
    program1()


if __name__ == "__main__":
    main()
