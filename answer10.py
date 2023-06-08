from datetime import date,datetime,timedelta

def daysBack(date,daysback):
    d1_obj = datetime.strptime(date, "%Y-%m-%d")
    difference=d1_obj-timedelta(days=daysback)
    final_date = difference.strftime("%Y-%m-%d")
    return final_date
    
   
from_year = int(input('Enter year in YYYY: '))
from_month = int(input('Enter month in MM: '))
from_day = int(input('Enter day in DD: '))

d1= date(from_year, from_month, from_day)
date_str = d1.strftime("%Y-%m-%d")
n = int(input('Enter number: '))
answer=daysBack(date_str,n)
print(answer)
