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

def countingValleys(n, s):
    isSeaLevel = True
    currentLevel = seaLevel = numberOfValleys = 0

    print(s)

    for step in s:
        if isSeaLevel:
            if step == 'U':
                currentLevel += 1

            if step == 'D':
                currentLevel -= 1
                numberOfValleys += 1

            isSeaLevel = False

        else:
            if step == 'U':
                currentLevel += 1

            if step == 'D':
                currentLevel -= 1

            if currentLevel == 0:
                isSeaLevel = True

    return numberOfValleys


n = int(input())

s = list(input())

print(countingValleys(n, s))
