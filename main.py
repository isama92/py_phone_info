import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input('Enter mobile number with country code: ')
mobileNo = phonenumbers.parse(mobileNo)

# get timezone
tz = timezone.time_zones_for_number(mobileNo)

# carrier
cr = carrier.name_for_number(mobileNo, 'en')

# region
region = geocoder.description_for_number(mobileNo, 'en')

# validation
valid = phonenumbers.is_valid_number(mobileNo)
valid_str = 'yes' if valid else 'no'
# possible number
possible = phonenumbers.is_possible_number(mobileNo)
possible_str = 'yes' if possible else 'no'


print('\ntimezone: %s\ncarrier: %s\nregion: %s\nvalid: %s\npossible: %s' % (tz, cr, region, valid_str, possible_str))
