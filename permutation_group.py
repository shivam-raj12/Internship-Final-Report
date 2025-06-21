from sympy.combinatorics import *

def stabilizer(group, element):
    print(f"Stabilizer({element + 1}): ")
    for x in group.stabilizer(element).generate_dimino():
        if x.is_identity:
            print("e")
        else:
            for permutation in x.cyclic_form:
                print(f"({','.join(str(permutation_element + 1) for permutation_element in permutation)})", end = "")
            print()


def generator(group):
    print(f"\nGenerator are: ")
    for x in group.generators:
        for y in x.cyclic_form:
            print(f"({', '.join(str(i+1) for i in y)})")


def main():
    size = int(input("Enter the size of the set: "))
    element = int(input("Enter an element of the set: "))

    if element not in range(1, size + 1):
        print(f"Element must be within {[x for x in range(1, size + 1)]}")
        return

    stabilizer(AlternatingGroup(size), element - 1)
    generator(AlternatingGroup(size))

if __name__ == "__main__":
    main()
