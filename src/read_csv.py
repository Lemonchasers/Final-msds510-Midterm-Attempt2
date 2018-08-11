import csv
import sys


def read_csv(input1):
    """The read_csv function within this file takes a csv and reads it into rows.
    Then we append the data so we have a list of rows."""
    c = open(input1)
    csv_c = csv.reader(c)
    rows = []

    for row in csv_c:
        rows.append(row)

    print(rows[161])

if __name__ == '__main__':
    read_csv(sys.argv[1])
