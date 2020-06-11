import calendar
year=int(input("Enter year: "))
month=int(input("Enter month: "))

mycal=calendar.month(year,month)
print(mycal)

#in this by default weekdays starts from Monday, we can change it by using this fn:-
calendar.setfirstweekday(calendar.SUNDAY)
mycal1=calendar.month(year,month)
print(mycal1)

#if you want to display all the months means whole calendar of a year then you can do that by using 
#this fn:-
yyyy=int(input("Enter the year to see its whole calendar: "))
mycal2=calendar.calendar(yyyy)
print(mycal2)

#TO check a year is leap year or not using the calendar module
yearleap=int(input("Enter the year to checkits leap year or not: "))
result=calendar.isleap(yearleap)
if result:
    print(f"Yes {yearleap} is a leap year")
else:
    print(f"Nope {yearleap} is not a leap year")