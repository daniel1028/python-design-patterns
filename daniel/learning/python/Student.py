class Student:
    def __init__(self,name,dept,college):
        self.name = name
        self.dept = dept
        self.college = college
    def display(self):
        print("name :",self.name, " dept:", self.dept," college: ", self.college)


s1 = Student("daniel","cse","oec")
s1.display()

