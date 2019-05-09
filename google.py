
from datetime import datetime
def get_gmt_time(city):
    now = datetime.utcnow()
    print(now)  #returns GMT time, like 2019-04-23 09:11:44.375078
    try:
        diff = gmt.getOffset(city)   #returns number of hours of offset for that city
    except:
        raise('Exception raised by API')
    dt = datetime.timedelta(diff, time=hours)
    return dt.hours,dt.minutes,dt.seconds,dt.milliseconds

get_gmt_time("california")