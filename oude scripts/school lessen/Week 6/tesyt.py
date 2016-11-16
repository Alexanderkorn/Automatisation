import pytz
from datetime import datetime

utc_tz = pytz.timezone('UTC')
utc_dt = datetime.now(utc_tz)

print(utc_dt)
