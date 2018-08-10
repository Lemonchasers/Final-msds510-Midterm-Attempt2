# 4d


import sys
import util
sys.path.insert(0, '/Users/lemonswilliams/'
                   'Documents/DSC 510/Week 6/msds510/src/msds510/')

records = [
                dict(year='1988', intro='Jun-88'),
                dict(year='1989', intro='May-89'),
                dict(year='2005', intro='5-May'),
                dict(year='2013', intro='13-Nov'),
                dict(year='2014', intro='14-Jan'),
                ]

for x in records:
    print("Input Record - ", x)
    print("Date joined - ",
          util.get_date_joined(x['year'], x['intro']))
    print("Days since joined - ",
          util.days_since_joined(x['year'], x['intro']))
    print()
