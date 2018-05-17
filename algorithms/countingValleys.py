# For every n steps:
# U - uphill
# D - downhill
# Start and end at sea level
# Each step is 1 unit change in altitude

# mountain - series of consecutive steps ABOVE sea level
#   - starts with up and ends with down to sea level

# valley - seq. steps BELOW sea level
#   - step down from sea level ends with step up to sea level

# find number of valleys walked through
# e.g. s = [D D U U U U D D] first enters valley 2 units deep then climbs mountain 2 units high

n = int(input())

s = list(input().strip().split(''))
