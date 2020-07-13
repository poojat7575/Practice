def print_triangle_left_justified(limit):
    for i in range(limit+1):
        print('* ' * i)


def print_triangle_right_justified(limit):
    n = limit * 2
    for i in range(limit+1):
        print(('* ' * i).rjust(n))


def print_pyramid(limit):
    n = limit
    for i in range(limit+1):
        print(' '*n, end='')
        print('* ' * i)
        n -= 1

def print_number_triangle(limit):
    for i in range(1, limit+1):
        print(" ".join(map(str, range(1, i+1))))

def print_increasing_number_triangle(rows):
    n = 1
    for i in range(1, rows+1):
        for j in range(i):
            print(n, end=' ')
            n += 1
        print()

if __name__ == "__main__":
    print_increasing_number_triangle(10)
    print_number_triangle(10)
    print_triangle_left_justified(10)
    print_triangle_right_justified(10)
    print_pyramid(10)
