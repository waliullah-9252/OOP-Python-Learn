class Student:
    def __init__(self,name,currnt_class,id) -> None:
        self.name = name
        self.current_class = currnt_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student Name: {self.name}, Class: {self.current_class}, Student Id: {self.id}'
    

class Teacher:
    def __init__(self,name,subject,id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher Name: {self.name}, Subject: {self.subject}, Teacher Id: {self.id}'


class School:
    def __init__(self,school_name) -> None:
        self.school_name = school_name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enrolled(self,name,fee):
        if fee <= 6500:
            return f'You cannot Enrolled !'
        else:
            id = len(self.students) + 1
            student = Student(name, 10, id)
            self.students.append(student)
            return f'{name} is enrolled and there id is {id}'
    
    def __repr__(self) -> str:
        print('Welcome to ', self.school_name)
        print('--------OUR TEACHER--------')
        for teacher in self.teachers:
            print(teacher)
        print('--------OUR STUDENT--------')
        for student in self.students:
            print(student)
        return 'All done'


# alia = Student('Alia Bhatt' , 10, 1)
# ranbeer = Teacher('Ranbir Kapor', 'Data Structure', 101)
# print(alia)
# print(ranbeer)

phitron = School('Phitron')
phitron.enrolled('Alia Bhatt', 5900)
phitron.enrolled('Rani', 9400)
phitron.enrolled('Tamim', 8000)
phitron.enrolled('Rahim Uddin', 6600)
phitron.enrolled('Karim Uddin', 6500)

phitron.add_teacher('Rahat Khan','Algorithm')
phitron.add_teacher('Abdullah Naim', 'Data Structure')
phitron.add_teacher('Jhankar Mahbub', 'Python and OOP')
phitron.add_teacher('Asif Mahmud', 'Database')

print(phitron)