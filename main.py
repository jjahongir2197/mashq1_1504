class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if grade >= 0 and grade <= 100:
            self.grades.append(grade)
        else:
            print("Noto'g'ri baho!")

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def max_grade(self):
        if len(self.grades) == 0:
            return 0
        return max(self.grades)

    def min_grade(self):
        if len(self.grades) == 0:
            return 0
        return min(self.grades)

    def show_info(self):
        print("Talaba:", self.name)
        print("Baholar:", self.grades)
        print("O'rtacha:", self.average())
        print("Eng katta:", self.max_grade())
        print("Eng kichik:", self.min_grade())


def main():
    s1 = Student("Ali")

    s1.add_grade(85)
    s1.add_grade(90)
    s1.add_grade(78)
    s1.add_grade(92)

    s1.show_info()


main()
