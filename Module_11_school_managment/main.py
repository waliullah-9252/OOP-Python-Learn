from school import School,ClassRoom,Subject
from person import Teacher,Student

def main():
    school = School('Adam Je', 'Uttra,Dhaka')

    # create some class room
    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # create some student
    abul = Student('Abul Mia',eight)
    school.student_addmission(abul)
    babul = Student('Babul Mia',eight)
    school.student_addmission(babul)
    kabul = Student('Kabul Mia',eight)
    school.student_addmission(kabul)

    # create some subject
    physics_teacher = Teacher('Abdul Goni')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Haradon Nag')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)

    biology_teacher = Teacher('Azmal Hossain')
    biology = Subject('biology', biology_teacher)
    eight.add_subject(biology)

    eight.take_semister_final()

    print(school)


if __name__ == '__main__':
    main()