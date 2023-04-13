import calendar
from datetime import timedelta

# <date> <time> TO <date> 00:00:00
truncate_to_morning: callable = lambda datetime_value: datetime_value.replace(
    hour=0, minute=0, second=0, microsecond=0
)
# <date> <time> TO <date> 59:59:59.99999
truncate_to_night: callable = lambda datetime_value: datetime_value.replace(
    hour=0, minute=0, second=0, microsecond=0
) + timedelta(days=1, microseconds=-1)

def month_week_info(dt):
    """
    Weekwise Calendar of a particular month .
    """
    __year = dt.year
    __month = dt.month
    return calendar.monthcalendar(__year,__month)
