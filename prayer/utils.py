import praytimes
from datetime import datetime

def calculate_prayer_times(latitude, longitude, date=None, tz=3):
    if date is None:
        date = datetime.now().date()
    
    pt = praytimes.PrayTimes()
    times = pt.getTimes(date, (latitude, longitude), tz)
    
    # Convert string times (e.g., "05:40") to time objects
    prayer_time_objects = {}
    for key in ['fajr', 'dhuhr', 'asr', 'maghrib', 'isha']:
        prayer_time_objects[key] = datetime.strptime(times[key], "%H:%M").time()
    
    return prayer_time_objects
