class Exam:
    def __init__(self,total_marks):
        self.total_marks = total_marks
        self.pass_mark = 33
        self.letter_mark = 80

    def grade(self):
        return self.letter_mark
    
    def result(self,marks):
        if marks >= 33:
            print('You will Pass this subject!')
        elif marks >= 80:
            print('You can pass & letter marks this subject')
        else:
            print('You can not pass this subject')

english = Exam(100)
english.result(55)
english.result(33)
english.result(32)
english.result(79)
english.result(80)
english.result(87)