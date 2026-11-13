from datetime import datetime

et = input('Enter event title: ')
ey = int(input('Enter year: '))
em = int(input('Enter month: '))
ed = int(input('Enter day: '))

print(' ') # under this processes the inputs to return their formatted versions

clean_et = et.upper().strip()
dt_str = f'{ey} {em} {ed}'

try:
    dt = datetime.strptime(dt_str, '%Y %B %d')
except ValueError:
    dt = datetime.strptime(dt_str, '%Y %m %d')

user_date = dt.strftime('%B %d, %Y')
formatted_month = dt.strftime('%B')
formatted_day = dt.strftime('%d')
formatted_year = dt.strftime('%Y')
formatted_weekday = dt.strftime('%A')

print('---Formatted Output---')

print(f'Event: {clean_et}')
print(f'Date: {user_date}')
print(f'Year: {formatted_year}')
print(f'Month: {formatted_month}')
print(f'Day: {formatted_day}')
print(f'Weekday: {formatted_weekday}')