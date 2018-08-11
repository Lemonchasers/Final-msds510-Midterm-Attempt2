import sys
from msds510 import util

"""The make_report.py fie has a main function. This function takes two arguments. 
The first is a csv file. The second is the location of the resulting mark down report.
The markdown report should include the top 10 avengers and some data about them."""


def main(input1,output2):
    with open(input1, 'r') as c:
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
        rep = strip.replace('/', '_').replace(' ', '_')
        fieldnames.append(rep)

    #3
    records = []

    for row in rows:
        dictionary = {}
        for field,value in zip(fieldnames, row):
            dictionary[field] = value

        records.append(dictionary)

    records = records[1::]

    for record in records:
        for key, value in record.items():
            if key.startswith('death'):
                if value == 'YES':
                    record[key] = True
                elif value == 'NO':
                    record[key] = False
            elif key.startswith('return'):
                if value == 'YES':
                    record[key] = True
                elif value == 'NO':
                    record[key] = False
            elif key.startswith('current'):
                if value == 'YES':
                    record[key] = True
                elif value == 'NO':
                    record[key] = False
            elif key in ['year', 'appearances']:
                record[key] = int(value)
            else:
                record[key] = value.strip()

    newlist = sorted(records, key=lambda k: k['appearances'], reverse=True)
    newlist[0:10]

    for record in newlist:
        for key, value in record.items():
            if key in ['appearances','year']:
                record[key] = str(value)

    newTemp = "# 1."+newlist[0]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[0]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[0]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[0]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[0]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[0]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 2."+newlist[1]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[1]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[1]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[1]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[1]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[1]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 3."+newlist[2]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[2]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[2]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[2]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[2]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[2]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 4."+newlist[3]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[3]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[3]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[3]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[3]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[3]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 5."+newlist[4]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[4]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[4]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[4]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[4]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[4]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 6."+newlist[5]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[5]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[5]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[5]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[5]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[5]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 7."+newlist[6]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[6]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[6]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[6]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[6]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[6]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 8."+newlist[7]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[7]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[7]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[7]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[7]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[7]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 9."+newlist[8]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[8]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[8]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[8]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[8]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[8]['url']+"\n"
    newTemp +="\n"

    newTemp += "# 10."+newlist[9]['name_alias']+"\n"
    newTemp +="\n"
    newTemp +="*Number of Appearances: "+newlist[9]['appearances']+"\n"
    newTemp +="*Year Joined: "+newlist[9]['year']+"\n"
    newTemp +="*Years Since Joining: "+newlist[9]['years_since_joining']+"\n"
    newTemp +="*Url: "+newlist[9]['url']+"\n"
    newTemp +="\n"
    newTemp +="##Notes: "+"\n"
    newTemp +=newlist[9]['url']+"\n"
    newTemp +="\n"

    with open(output2, 'w') as output:
        output.write(newTemp)


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
