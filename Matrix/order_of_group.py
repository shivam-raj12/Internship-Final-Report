"""
This program returns the order of 2 x 2 Z_p matrix.
"""
def get_order_of_GL_group(p):
    return (p * p - 1) * (p * p - p)

def main():
    p = int(input("Enter the value of p for GL(2, Z_p) group: "))
    print("The order of group GL(2, Zₚ) is", get_order_of_GL_group(p))

if __name__ == '__main__':
    main()