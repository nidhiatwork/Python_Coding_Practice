from datetime import date, time, datetime, timedelta

date = date.today()
print(date)
print(date.day, date.month, date.year, date.weekday())

time = time(12,30,00)
print(time)
print(time.hour, time.minute, time.second)

dt = datetime.now()
print(dt)
print(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second, dt.weekday())
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days[dt.weekday()])
#formatting for day and month
print(dt.strftime("%a, %A, %w, %H, %I, %M, %S, %p, %c, %X, %d/%m/%y, %A %d, %B %Y"))
print(dt.strftime("%a, %A, %w, %d"))

#formatting for time
print(dt.strftime("%H, %I, %M, %S, %p"))
#locale specific date and time
print(dt.strftime("%c, %X"))


#long date format
print(dt.strftime("%A %d, %B %Y"))

#short date and time
print(dt.strftime("%m/%d/%y %I:%M %p"))

#Modifying dates and times
date = date.replace(day=12, month=5, year=2020)
time = time.replace(hour=9, minute=6, second=10)
dt = dt.replace(day=12, month=5, year=2017, hour=9, minute=6, second=10)
print(date,time,dt)

# Creating any date from calender
dt = datetime(2019,1,15,10,23,44) #year, month and then day, hour, minute, second
print(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second, dt.weekday())

#Calculations on date and time
dt1 = datetime(2019,1,15)
dt2 = datetime(2019,1,20,15)
print(dt1<dt2)

delta = dt2-dt1
print(delta)
print(delta.days, delta.seconds)

now = datetime.now()
oneyear = timedelta(days=365)
oneweek = timedelta(weeks=1)
print("one year from now", now+oneyear)
print("one year ago", now-oneyear)
print("one week from now", now-oneweek)
print(oneyear.total_seconds())