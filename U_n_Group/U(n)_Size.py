from math import sqrt

'''
This function returns the size of U(n) group.
'''
def get_coprime_size(n):
    size = n
    prime_divisor = set()  # Stores the prime divisor of n. It is a set so that it won't store the same value twice.

    while n % 2 == 0:  # If 2 divides the n, store it to prime divisor and keep dividing n by 2 until it is not divisible by 2.
        prime_divisor.add(2)
        n = n // 2

    for i in range(3, int(sqrt(n)) + 1, 2):  # Starts the loop from 3 and increase it by 2 always because now the n is not divisible by any even number.
        while n % i == 0: # If it is divisible by i, then store i in prime divisor and keep dividing n until it is not divisible by i. This way we will make sure it is not divisible by i and i multiples also.
            prime_divisor.add(i)
            n = n // i

    if n > 1: # Finally if n is greater than 1, it means it is also a prime divisor because we already removed all the divisors.
        prime_divisor.add(n)

    for x in prime_divisor: # Going through all the elements of prime divisor of n.
        size *= ((x - 1) / x) # Calculating the size of U(n) group using the formula.

    return int(size)  # Finally returning the calculated U(n) group order.


def main():
    n = int(input("Enter the value of n for U(n) group: "))
    print(f"|U({n})| = {get_coprime_size(n)}")

if __name__ == '__main__':
    main()