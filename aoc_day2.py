import sys
from expense_report_list import my_expense_report


def day2():
    for i in my_expense_report:
        for j in my_expense_report:
            if i + j < 2020 and min(my_expense_report) <= 2020 - (i+j):
                for y in my_expense_report:
                    if y == i:
                        y += 1
                    if y == j:
                        y += 1
                    if y + j + i == 2020:
                        print(f'found it!! {y} {j} {i} {i * j* y}')
                        sys.exit()
            else:
                print(f'Nope.. Next {i}')
    sys.exit()


if __name__ == '__main__':
    day2()
