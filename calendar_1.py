import calendar
year=int(input("year:"))
month=int(input("month:"))
month_name=(input("month name:"))
month_calendar=calendar.month(year,month)
month_calendar=month_calendar.replace(calendar.month_name[month],month_name)
print(month_calendar)