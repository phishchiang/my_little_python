import datetime
import pytz

'''
d = datetime.date.today()
tdelta = datetime.timedelta(days = 7)
print (d - tdelta)
print (tdelta.total_seconds())
'''

# dt = datetime.datetime(2018, 5, 2, 22, 30, 45, tzinfo=pytz.UTC)
dt_now = datetime.datetime.now(tz=pytz.UTC) # Current time with GMT +0 time zone
print (dt_now)

dt_tw = dt_now.astimezone(pytz.timezone('ROC')) # Taipei GMT +8
print (dt_tw)

# show the datetime with format code : strftime = datetime to string
print (dt_tw.strftime('%B %d, %Y'))

# convert from string to datetime : strptime = string to datetime
dt_str = 'July 26, 2016'
convertDt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print (convertDt)



'''
# Show all the timezones
for tz in pytz.all_timezones:
  print (tz)
'''