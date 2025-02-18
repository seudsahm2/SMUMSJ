from django import template
from hijri_converter import convert
from datetime import datetime

register = template.Library()


@register.filter
def hijri_date(value):
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            return value  # Return the original value if it cannot be parsed
    hijri_date = convert.Gregorian(
        value.year, value.month, value.day).to_hijri()
    return f"{hijri_date.day} {hijri_date.month_name()} {hijri_date.year}"
