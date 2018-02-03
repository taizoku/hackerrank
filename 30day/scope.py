class Difference:
    def __init__(self, a):
        self.__elements = a
        
        #mcode



# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)