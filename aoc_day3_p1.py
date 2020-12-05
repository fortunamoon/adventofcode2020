from aoc_day3_p1_data import my_slopes
# 31 characters & 323 rows
# Still get a division by zero but it works.


def tree_counting():
    set_x = int(input('Enter the X plane setting:'))
    set_y = int(input('Enter the Y plane setting:'))

    with open('slopes.txt') as file:
        slope_matrix = file.read().split("\n")[::set_y]
    k = 0
    tree_count = 0
    for y in slope_matrix:
        tree_count += (y[k % len(y)] == '#')
        k += set_x
        print(f'There are {tree_count} trees in your way!')


if __name__ == '__main__':
    tree_counting()
