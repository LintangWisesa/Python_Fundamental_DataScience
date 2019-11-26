from datetime import datetime
from dateutil import tz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Jakarta')

utc = datetime.utcnow()
print(utc)

utc = utc.replace(tzinfo=from_zone)
local = utc.astimezone(to_zone)
print(local)