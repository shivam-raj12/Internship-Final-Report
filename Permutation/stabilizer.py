from sympy.combinatorics import AlternatingGroup, SymmetricGroup


'''
This program prints the stabilizer of a point.
'''
def stabilizer(group, element):
    print(f"Stabilizer({element + 1}): ")
    for x in group.stabilizer(element).generate_dimino():
        if x.is_identity:
            print("e")
        else:
            for permutation in x.cyclic_form:
                print(f"({', '.join(str(permutation_element + 1) for permutation_element in permutation)})", end = "")
            print()


def main():
    n = int(input("Enter the value of n for S_n group: "))
    element = int(input("Enter an element of the set: "))

    if element not in range(1, n + 1):
        print(f"Element must be within {[x for x in range(1, n + 1)]}")
        return

    stabilizer(SymmetricGroup(n), element - 1) # Here we can replace `SymmetricGroup(n)` by `AlternatingGroup(n)` to get stabilizer point of Alternating group.

if __name__ == "__main__":
    main()
