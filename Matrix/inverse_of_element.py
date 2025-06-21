"""
This program prints inverse of 2 x 2 Z_p matrix.

Here a, b, c, d are represented as:
            ⸺        ⸺
            |  a    b  |
            |  c    d  |
            ⸺        ⸺

      where a, b, c, d are the elements of Z_p group.
"""
def find_inverse(a, b, c, d, p):
    global inverse_detA_in_Zp
    detA = a * d - b * c
    detA_in_Zp = detA % p
    for x in range(1, p + 1):
        if x * detA_in_Zp % p == 1:
            inverse_detA_in_Zp = x

    _a = d * inverse_detA_in_Zp
    _b = -b * inverse_detA_in_Zp
    _c = -c * inverse_detA_in_Zp
    _d = a * inverse_detA_in_Zp

    _a = _a % p if _a >= p or _a < 0 else _a
    _b = _b % p if _b >= p or _b < 0 else _b
    _c = _c % p if _c >= p or _c < 0 else _c
    _d = _d % p if _d >= p or _d < 0 else _d

    print("⸺        ⸺")
    print(f"| {_a}     {_b}  |")
    print(f"| {_c}     {_d}  |")
    print("⸺        ⸺")

def main():
    print("⸺        ⸺")
    print("|  a    b  |")
    print("|  c    d  |")
    print("⸺        ⸺")

    a = int(input("a value:  "))
    b = int(input("b value:  "))
    c = int(input("c value:  "))
    d = int(input("d value:  "))
    p = int(input("Zₚ value (p must be prime):  "))

    find_inverse(a, b, c, d, p)

if __name__ == '__main__':
    main()
