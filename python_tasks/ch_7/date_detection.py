import re

date=re.compile(r'''(
                (\d{2})         #day
                (\W|/|.*)?          #seperator
                (\d{2})         #month
                (\W|/|.*)?          #seperator
                (\d{4})         #year
                )''',re.VERBOSE)
mo=date.search("number is : 12/12/2004")
day = int(mo.group(2))
month = int(mo.group(4))
year = int(mo.group(6))
print(mo.groups())


calender={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def date_check():
    if month!=2:

        if month in calender:
            x=calender.get(month,)
            if day <= x:
                return ("valide date")
        else:
            return("invalid")
    else:
        if day==28 and year%4==0:
            return ("valid date")
        else:
            return("return false")

print(date_check())


