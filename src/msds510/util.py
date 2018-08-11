import datetime
import csv
import sys

"""This util.py file consists of many functions. Thus, this file
acts as a library of functions that we can import into other .py files
and use. Therefore if we wanted to not repeat ourselves as much, we 
could store a function here, import said function into a .py file and
have a more efficient front facing .py file."""

numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"


def get_month(input1):
    if input1[0] in numbers:
        month_number = datetime.datetime.strptime(input1, '%d-%b').month
    elif input[0] in letters:
        month_number = datetime.datetime.strptime(input1, '%b-%y').month
    else:
        month_number = ""
    return month_number


def get_date_joined(input2, input3):
    yearss = int(input2)

    if input3[0] in numbers:
        month_numbers = datetime.datetime.strptime(input3, '%d-%b').month
    else:
        month_numbers = datetime.datetime.strptime(input3, '%b-%y').month

    day = 1

    date1 = datetime.date(yearss, month_numbers, day)
    date2 = datetime.datetime.combine(date1,datetime.time())
    date3 = date2.date()
    return date3


def days_since_joined(input4, input5):
    yearss = int(input4)

    if input5[0] in numbers:
        month_numbers = datetime.datetime.strptime(input5, '%d-%b').month
    else:
        month_numbers = datetime.datetime.strptime(input5, '%b-%y').month

    day = 1

    date1 = datetime.date(yearss, month_numbers, day)
    date2 = datetime.datetime.combine(date1,datetime.time())
    date3 = date2.date()
    today = datetime.date.today()

    result1 = abs(today - date3).days
    return result1


def read_csv(input1):
    """The read_csv function within this file takes a csv and reads it into rows.
    Then we append the data so we have a list of rows."""
    c = open(input1)
    csv_c = csv.reader(c)
    rows = []

    for row in csv_c:
        rows.append(row)


def write_csv(input1, output2):
    c = open(input1, 'r', newline='')
    csv_c = csv.DictReader(c, delimiter=',')
    rows = []

    for row in csv_c:
        roww = row.split(',')
        if len(row) == 21:
            rows.append(roww)

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


def convert_to_utf8_t1(input1):

    """ The convert_to_utf8 function within this file converts a csv to a utf8 csv file.
    It takes two arguments, the file directory that needs to be converted and the file
    directory to output the file."""

    with open(input1, 'rb') as a:
        avengers = a.read()
    avengers_decoded = avengers.decode('iso-8859-1')
    avengers_encoded = avengers_decoded.encode('utf8')
    return avengers_encoded
