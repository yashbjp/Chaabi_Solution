from datetime import date,datetime

def fromToDiff(from_date,to_date,diff):
    d1_obj = datetime.strptime(from_date, "%Y-%m-%d")
    d2_obj = datetime.strptime(to_date, "%Y-%m-%d")
    difference=d2_obj-d1_obj
    
    if diff>difference.days:
        return True
    return False
    
    
from_year = int(input('Enter from_year in YYYY: '))
from_month = int(input('Enter  from_month in MM: '))
from_day = int(input('Enter from_day in DD : '))

d1= date(from_year, from_month, from_day)

from_date_time_str = d1.strftime("%Y-%m-%d")

to_year = int(input('Enter to_year in YYYY: '))
to_month = int(input('Enter to_month in MM: '))
to_day = int(input('Enter to_day in DD: '))

d2= date(to_year, to_month, to_day)

to_date_time_str = d2.strftime("%Y-%m-%d")

diff = int(input('Enter difference: '))

answer=fromToDiff(from_date_time_str,to_date_time_str,diff)
print(answer)