class Difference:


    def __init__(self, int_array):
        self.__elements = int_array
        self.maximumDifference = 0

    def computeDifference(self):
        self.__elements = sorted(self.__elements)
        self.maximumDifference = abs(self.__elements[0] - self.__elements[-1])
        return self.maximumDifference


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)