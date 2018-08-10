import sys


sys.path.insert(0, '/Users/lemonswilliams/Documents/DSC 510/Midterm/msds510/src/msds510/')
import util

import csv
input1 = sys.argv[1]
output2 = sys.argv[2]

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
    #2
    header = rows[0]
    fieldnames = []

    for name in header:
        lower = name.lower()
        strip = lower.strip('\n').strip('?')
        rep = strip.replace('/','_').replace(' ','_')
        fieldnames.append(rep)

    #3
    records = []

    for row in rows:
        dictionary = {}
        for field,value in zip(fieldnames,row):
            dictionary[field] = value

        records.append(dictionary)
    records = records[1::]

    #for x in records:
    #   x['month_joined'] = util.get_month(x['full_reserve_avengers_intro'])

    #writeoutpart
    with open(output2, "w") as csvfile:
        fieldnames = ['url', 'name_alias', 'appearances', 'current', 'gender', 'probationary_introl', 'full_reserve_avengers_intro', 'year', 'years_since_joining', 'honorary', 'death1', 'return1', 'death2', 'return2', 'death3', 'return3', 'death4', 'return4', 'death5', 'return5', 'notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for roww in records:
            writer.writerow(roww)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
