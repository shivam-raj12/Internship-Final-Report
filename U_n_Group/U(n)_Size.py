from math import gcd

'''
This function returns the size of U(n) group.
'''
def get_coprime_size(size):
    count = 0
    for i in range(1, size):
        if gcd(i, size) == 1:
            count += 1
    return count

def main():
    n = int(input("Enter the value of n for U(n) group: "))
    print(f"|U({n})| = {get_coprime_size(n)}")

if __name__ == '__main__':
    main()