# HackerLand Enterprise is adopting a new viral advertising strategy.
# When they launch a new product, they advertise it to exactly 5 people on social media.

# On the FIRST day, HALF of those 5 people
# *(ie floor(5/2) = 2)
# like it and share with 3 of their friends

# At the beginning of the SECOND day
# floor(5/2) * 3 = 2*3 = 6 people have received the advertisement

# EACH day, floor(recipients/2) of the recipients like the advertisement and will share with 3 friends the following day

# ----------------------------------------------------------------------------------------------------------------------

# Assuming nobody receives the advertisement twice,
# Determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.

# ----------------------------------------------------------------------------------------------------------------------

# EXAMPLE: how many have liked the ad by the end of the 5th day
# Day Shared Liked Cumulative
# 1      5     2       2
# 2      6     3       5
# 3      9     4       9
# 4     12     6      15
# 5     18     9      24

# The cumulative number of likes is 24.


def viralAdvertising(numDays):
    numLikes = 0
    recipients = 5
    for day in range(1, numDays+1):
        print(day)
        likedAd = recipients // 2
        sharedAd = likedAd * 3
        numLikes += likedAd
    return numLikes


# INPUT
# 1. A single integer, n, denoting a number of days.
numDays = int(input())

# OUTPUT
# Print the number of people who liked the advertisement during the first n days.
print(viralAdvertising(numDays))