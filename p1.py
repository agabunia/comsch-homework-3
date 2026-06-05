from itertools import permutations, combinations
from datetime import date, timedelta
import calendar

# Exc 1
word = 'ABCD'

def permut(word):
    perms = [''.join(p) for p in permutations(word)]

    for p in perms:
        print(p)
    
    print(len(perms))

# permut(word)


# Exc 2
def next_tuesday():
    today = date.today()
    days_until_next_monday = 7 - today.weekday()
    next_monday = today + timedelta(days=days_until_next_monday)
    tuesday = next_monday + timedelta(days=1)
    return tuesday

# print(next_tuesday())


# Exc 3
def is_leap_year(year):
    # return calendar.isleap(year) ## python had builtin function for this
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) # Oldschool

# user_input_year = int(input("Enter a year: "))
# print(is_leap_year(user_input_year))


# Exc 4
def weeks_until_new_year():
    today = date.today()
    new_year = date(today.year + 1, 1, 1)
    days_left = (new_year - today).days
    weeks_left = days_left // 7
    return weeks_left

# print(weeks_until_new_year())


# Exc 5
def three_element_combinations(items):
    combos = list(combinations(items, 3))

    for c in combos:
        print(c)
    
    print(len(combos))

# three_element_combinations([1, 2, 3, 4, 5])


# Exc 6
def all_combinations(text):
    combos = []

    for length in range(1, len(text) + 1):
        for c in combinations(text, length):
            combos.append(''.join(c))
    
    for c in combos:
        print(c)

# all_combinations("XYZ")


