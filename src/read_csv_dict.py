# 3b
import sys

input1 = sys.argv[1]


def main(input1):
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
    print(records[161])


if __name__ == '__main__':
    main(sys.argv[1])
