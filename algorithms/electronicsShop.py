# monica wants to spend as much money as she can
# if she doesn't have enough for BOTH print -1

# e.g. s = 60
# keyboards = [40, 50, 60]
# usb drive = [5,  8,  12]
# possible to purchase 40k + 12usb = 52
# or higher is then 50k + 8usb = 58

# input:
# FIRST LINE (3 space sep integers)
#   - budget
#   - num of keyboards
#   - num of usb models
budget, numKeyboards, numUSB = map(int, input().strip().split(' '))

# SECOND LINE
#   n space separated integers keyboard[i]
#   - prices of each keyboard model


# THIRD LINE
#   m space separated integers keyboard[i]
#   - prices of each USB drive
