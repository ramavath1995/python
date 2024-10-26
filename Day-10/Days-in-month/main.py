month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400:
                return True
            else:
                return False
        else:
            return True
    return False


year = int(input("Enter a year: "))
month = int(input("Which month do you want to check: "))


def days_in_month(b, m):
    if b and m == 2:
        return 29
    else:
        return month_days[m - 1]


print(f"Year {year} has {days_in_month(is_leap(year), month)} days")
