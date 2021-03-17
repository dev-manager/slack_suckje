class Slack:
    @staticmethod
    def star(x, text):
        for i in range(1, x):
            print('　' * (x - i), end='')
            print(text * i, end='')
            print('\n')
        for j in range(x):
            print('　' * j, end='')
            print(text * (x - j), end='')
            print('\n')


if __name__ == '__main__':
    Slack.star(10, '고소')
