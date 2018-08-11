import sys
import csv

"""The write_csv.py file consists of one function write_csv.
The purpose of the function is to take two arguments. The first argument
is the file path for a a csv file that you wish to process like the raw avengers data set.
Then the  second argument is the file location of the processed csv file for argument 1."""


def write_csv(input1, output2):
    with open(input1, 'r') as c:
        lines = c.readlines()

    rows = []
    for x in lines:
        row = x.split(',')
        if len(row) == 21:
            rows.append(row)
    # 2
    header = rows[0]
    fieldnames = []

    for name in header:
        lower = name.lower()
        strip = lower.strip('\n').strip('?')
        rep = strip.replace('/', '_').replace(' ', '_')
        fieldnames.append(rep)

    # 3
    records = []

    for row in rows:
        dictionary = {}
        for field, value in zip(fieldnames, row):
            dictionary[field] = value

        records.append(dictionary)

    # write out part
    with open(output2, "w") as csvfile:
        fieldnames = records[0]
        records = records[1:]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for roww in records:
            writer.writerow(roww)


if __name__ == '__main__':
    write_csv(sys.argv[1], sys.argv[2])
