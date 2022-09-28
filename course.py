# To get current date and time
# We need to use the datetime library
from datetime import datetime, timedelta

today = datetime.now()
# Function returns a datetime object
print(f'1.  Today is: {str(today)}')

# timedelta is used to define a period fof time
one_day = timedelta(days=1)
yesterday = today - one_day
print(f'2.  Yesterday was: {str(yesterday)}')

print(f'Day: {str(today.day)}')
print(f'Month: {str(today.month)}')
print(f'Year: {str(today.year)}')

birthday = input('What is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y') #Strptime stores the date as an object
print(f'Birthday: {str(birthday_date)}')
a_day = timedelta(days=1)
day_before = birthday_date - a_day
print(f'Day before birthday: {str(day_before)}')

# Continuing from Episode 16