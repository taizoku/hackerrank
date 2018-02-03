class Difference:
    def __init__(self, a):
        self.__elements = a
        
        #mcode

    def __init__(self, N):
        self.__elements = N
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = abs(self.__elements[1] - self.__elements[0])
        return self.maxmimumDifference
# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)