from math import gcd


def get_coprime_size(size):
    count = 0
    for i in range(1, size):
        if gcd(i, size) == 1:
            count += 1
    return count


def get_size_of_aut(size):
    return size * get_coprime_size(size)


def main():
    size = int(input("Value of n for Dₙ: "))
    print(f"|Aut(Dₙ)| = {get_size_of_aut(size)}")


if __name__ == '__main__':
    main()
