class Student:
    def __init__(self,name,current_class,id) -> None:
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student name: {self.name} and there current class: {self.current_class} there Student id: {self.id}'
    

class Teacher:
    def __init__(self,name,subjet,id) -> None:
        self.name = name
        self.subject = subjet
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher name: {self.name} and Subject: {self.subject} and Teacher Id: {self.id}'
    



class School:
    def __init__(self,school_name) -> None:
        self.school_name = school_name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee <= 6500:
            return 'You cannot enrolled this course!'
        else:
            id = len(self.students) + 1
            student = Student(name,10,id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id} ,back extra money {fee - 6500}'
    
    def __repr__(self) -> str:
        print(f'Welcome to {self.school_name}')
        print('----------OUR TEACHERS----------')
        for teacher in self.teachers:
            print(teacher)
        print('----------OUR STUDENTS----------')
        for student in self.students:
            print(student)
        return 'All done now'



# rahim = Student("Rahim Uddin", 10, 1)
# abdul = Teacher('Abdul Goni', 'Data Structur', 101)
# print(rahim)
# print(abdul)


phitron = School('Phitron')
phitron.enroll('Rahim Udiin', 7000)
phitron.enroll('Karim Udiin', 5800)
phitron.enroll('Solim Udiin', 7890)
phitron.enroll('Shorif Udiin', 7300)

phitron.add_teacher('Rahat Khan', 'Algorithm')
phitron.add_teacher('Abdullah Naim', 'Data Structure')
phitron.add_teacher('Jhankar Mahbub', 'Python & OOP')
phitron.add_teacher('Asif Mahmud', 'Database')

print(phitron)