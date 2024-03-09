#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2024
Program: assign1.py (replace student_id with your Seneca User name)
Author: "Farnoosh Rahmati"
Student ID: frahmati1
The python code in this file (assign1.py) is original work written by
"Farnoosh Rahmati". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.


Date: 08-03-2024
'''

import sys

def usage():
    return "Usage: assign1.py DD-MM-YYYY N"

def days_in_mon(year):
    is_leap = leap_year(year)
    return {1: 31, 2: 29 if is_leap else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def valid_date(date):
    try:
        day, month, year = map(int, date.split('-'))
        if month < 1 or month > 12:
            return False, "Error: wrong month entered"
        if day < 1 or day > days_in_mon(year)[month]:
            return False, "Error: wrong day entered"
        return True, ""
    except ValueError:
        return False, "Error: wrong date entered"

def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def after(today):
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        mon_max = days_in_mon(year)
        tmp_day = day + 1 # next day

        if tmp_day > mon_max[month]:
            tmp_day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1

        next_date = str(tmp_day).zfill(2) + "-" + str(month).zfill(2) + "-" + str(year)
        return next_date

def before(today):
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        if day > 1:
            day -= 1
        else:
            month -= 1
            if month < 1:
                month = 12
                year -= 1
            day = days_in_mon(year)[month]

        prev_date = str(day).zfill(2) + "-" + str(month).zfill(2) + "-" + str(year)
        return prev_date

def dbda(start_date, num_days):
    is_valid, message = valid_date(start_date)
    if not is_valid:
        return message
    
    end_date = start_date
    if num_days > 0:
        for _ in range(num_days):
            end_date = after(end_date)
    elif num_days < 0:
        for _ in range(-num_days):
            end_date = before(end_date)
    
    return end_date

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(usage())
        sys.exit(1)
    
    date_arg, days_arg = sys.argv[1], sys.argv[2]
    try:
        days_int = int(days_arg)
        is_valid, message = valid_date(date_arg)
        if not is_valid:
            print(message)
            sys.exit(1)
        result = dbda(date_arg, days_int)
        print(result)
    except ValueError:
        print("Error: The number of days must be an integer.")
        sys.exit(1)


