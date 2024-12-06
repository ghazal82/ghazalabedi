import calendar
year=int(input("year:"))
month=int(input("month:"))
month_farsi=["","farvardin","ordibehesht","khordad","tir","mordad","shahrivar","mehr","aban","azar","dey","bahman","esfand"]
month_name_farsi=month_farsi[month]
print(f"   {month_name_farsi}","(",month,")",f" {year}",sep="" )
calendar.setfirstweekday(5)
print(calendar.month(year,month))
