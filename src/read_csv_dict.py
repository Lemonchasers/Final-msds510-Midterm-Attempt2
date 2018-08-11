import csv
import sys


def read_csv_dict(input1):
    """The read_csv_dict function within this file takes a csv and reads it into a list of dictionaries.
    Then it prints the 161st record."""
    c = open(input1)
    csv_c = csv.DictReader(c)
    records = []

    for record in csv_c:
        records.append(record)

    print(records[160])


if __name__ == '__main__':
    read_csv_dict(sys.argv[1])

