# file for definitions of some useful functions

def print_matrix_nb(m):
    for row in range(len(m)):
        for col in range(len(m[row])):
            print(m[row][col].number, end=" ")
        print('\n')


def convertbinaire(x, k):
    """convert integers(int), between 0 and 2^k-1, into binary(string), on k digits."""
    result = ""
    while x != 0:
        result = str(x % 2) + result
        x //= 2
    result = '0'*(k-len(result)) + result
    return result
