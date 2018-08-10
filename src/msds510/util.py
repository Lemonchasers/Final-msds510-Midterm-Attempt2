#a
import datetime


numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"

def get_month(input1):
    if input1[0] in numbers:
        month_number = datetime.datetime.strptime(input1, '%d-%b').month
        #print(month_number)
    elif input[0] in letters:
        month_number = datetime.datetime.strptime(input1, '%b-%y').month
    else:
        month_number = ""
        #print(month_number)
    return month_number
#if __name__ == '__main__':
#                get_month(sys.argv[1])

#print(get_month('Nov-89'))


#b

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
    #print(date3)

#print(get_date_joined('1988', 'Jun-88'))


#c

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
    #print(result1)

#print(days_since_joined('1988', 'Jun-88'))

if __name__ == "__main__":
    import sys
    util(int(sys.argv[1]))
