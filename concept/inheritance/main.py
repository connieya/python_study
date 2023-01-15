class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(f'제 이름은 {self.name} 입니다.')

    def get_age(self):
        print(f"제 나이는 {self.age}세 입니다.")


class Student(Person):
    def __init__(self, name, age, GPA):
        super().__init__(name, age)
        self.GPA = GPA

    def get_name(self):
        print(f"저는 대학생 {self.name} 입니다.")

    def get_GPA(self):
        print(f"제 학점은 {self.GPA} 입니다.")


student_a = Student('건희',29,4.3)
# student_a.get_name()
# student_a.get_age()
student_a.get_GPA()