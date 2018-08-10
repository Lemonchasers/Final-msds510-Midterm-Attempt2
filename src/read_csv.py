import sys

input1 = sys.argv[1]


def main(input1):
    with open(input1, 'r') as c:
        rows = c.readlines()

    print(rows[161])


if __name__ == '__main__':
    main(sys.argv[1])
