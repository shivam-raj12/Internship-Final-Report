from Matrix.order_of_group import get_order_of_GL_group

'''
This program prints the order of 2 x 2 Z_p matrix.

Here a, b, c, d are represented as:
            ⸺        ⸺
            |  a    b  |
            |  c    d  |
            ⸺        ⸺
            
      where a, b, c, d are the elements of Z_p group.      

'''
def order_of_Zp_matrix_element(a, b, c, d, p):
    if a == 1 and b == 0 and c == 0 and d == 1:
        print("Order is: 1")
        return

    temp_a, temp_b, temp_c, temp_d = a, b, c, d

    order_of_group = get_order_of_GL_group(p)
    for x in range(2, order_of_group + 1):
        _a = (a * temp_a) + (b * temp_c)
        _b = (a * temp_b) + (b * temp_d)
        _c = (c * temp_a) + (d * temp_c)
        _d = (c * temp_b) + (d * temp_d)

        _a = _a % p if _a >= p or _a < 0 else _a
        _b = _b % p if _b >= p or _b < 0 else _b
        _c = _c % p if _c >= p or _c < 0 else _c
        _d = _d % p if _d >= p or _d < 0 else _d

        if _a == 1 and _b == 0 and _c == 0 and _d == 1:
            print(f"Order is: {x}")
            break
        else:
            temp_a, temp_b, temp_c, temp_d = _a, _b, _c, _d

        if x == order_of_group:
            print(f"Given matrix is not invertible in Z{p}")


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

    order_of_Zp_matrix_element(a, b, c, d, p)


if __name__ == '__main__':
    main()
