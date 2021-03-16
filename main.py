
def star(x):
    for i in range(1, x):
        print('　' * (x - i), end='')
        print('고소' * i, end='')
        print('\n')
    for j in range(x):
        print('　' * j, end='')
        print('고소' * (x - j), end='')
        print('\n')


if __name__ == '__main__':
    star(10)
