from U_n_Group.U_n_Size import get_coprime_size


'''
This function returns the order of the group Aut(D_n)
'''
def get_size_of_aut(size):
    return size * get_coprime_size(size)


def main():
    size = int(input("Value of n for Dₙ: "))
    print(f"|Aut(Dₙ)| = {get_size_of_aut(size)}")


if __name__ == '__main__':
    main()
