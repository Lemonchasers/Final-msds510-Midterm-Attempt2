import sys
import csv

""" The process_csv.py file consists of a main function that requires two arguments
The first argument is the file path for an input csv file. The second argument is 
the file path for the results of processing the input csv file.
The main function provides python friendly header names for the columns.
"""


def main(input1,output2):
    with open(input1,'rb') as a:
        avengers = a.read()

    avengers_decoded = avengers.decode('iso-8859-1')
    avengers_encoded = avengers_decoded.encode('utf8')

    tempinput = "/Users/lemonswilliams/Documents/DSC 510/Midterm/msds510/data/interim/avengers_utf8.csv"

    with open(tempinput, 'wb') as b:
        b.write(avengers_encoded)

    with open(tempinput,'r') as c:
        lines = c.readlines()

    rows = []
    for x in lines:
        row = x.split(',')
        if len(row) == 21:
            rows.append(row)
    header = rows[0]
    fieldnames = []

    for name in header:
        lower = name.lower()
        strip = lower.strip('\n').strip('?')
        rep = strip.replace('/','_').replace(' ','_')
        fieldnames.append(rep)

    records = []

    for row in rows:
        dictionary = {}
        for field,value in zip(fieldnames,row):
            dictionary[field] = value

        records.append(dictionary)

    with open(output2, "w") as csvfile:
        fieldnames = records[0]
        records = records[1:]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for roww in records:
            writer.writerow(roww)


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
