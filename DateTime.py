import datetime

today = datetime.datetime.now()

print(today)


meeting_date = datetime.date(2021, 10, 5)

print(meeting_date)

meeting = datetime.datetime(2021, 10, 5, 10, 5, 31)

print(meeting)


# Day
a = datetime.datetime.now()
print(a.year)
print(a.strftime("%A"))

# Short Day
print(a.strftime("%a"))

# Date
print(a.strftime("%d"))

# Month
print(a.strftime("%b"))
