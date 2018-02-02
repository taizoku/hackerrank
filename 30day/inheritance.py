class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # Class Constructor
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.

    def __init__(self, first_name, last_name, id_num, scores_array):
        super(Student, self).__init__(first_name, lastName, id_num)
        self.firstName = first_name
        self.lastName = last_name
        self.id = id_num
        self.scores = scores_array


#   Function Name: calculate
#   Return: A character denoting the grade.
#
    def calculate(self):
        average = 0
        for result in self.scores:
            average += result
        average /= len(scores)

        if 90 <= average <= 100:
            grade = 'O'
        elif 80 <= average < 90:
            grade = 'E'
        elif 70 <= average < 80:
            grade = 'A'
        elif 55 <= average < 70:
            grade = 'P'
        elif 40 <= average < 55:
            grade = 'D'
        else:
            grade = 'T'

        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
