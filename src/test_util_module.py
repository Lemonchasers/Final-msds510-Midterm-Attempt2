from msds510 import util

"""The test_util_module.py file imports all functions from the file util.py
in the subfolder msds510. More specifically we then use the get_date_joined function
and the days_since_joined function."""

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
