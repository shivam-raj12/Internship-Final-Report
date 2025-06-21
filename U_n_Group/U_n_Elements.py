from math import gcd

'''
This function returns a list of all the elements of U(n) group.
'''
def get_all_elements_list(size):
    elements = []
    for x in range(1, size):
        if gcd(x, size) == 1:
            elements.append(x)
    return elements

def main():
    n = int(input("Enter the value of n for U(n) group: "))
    print(f"U({n}) = {get_all_elements_list(n)}")
if __name__ == '__main__':
    main()
