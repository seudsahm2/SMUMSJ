from django.utils import timezone
from .utils import calculate_prayer_times

def prayer_times(request):
    latitude = 9.03  # Latitude for Addis Ababa
    longitude = 38.74  # Longitude for Addis Ababa
    current_date = timezone.now().date()
    
    # Calculate prayer times
    calculated_prayer_times = calculate_prayer_times(latitude, longitude, current_date)
    
    return {
        'current_date': current_date,
        'calculated_prayer_times': calculated_prayer_times,  # Return under the expected key
    }
