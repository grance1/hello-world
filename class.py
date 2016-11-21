#!/usr/bin/python2.7
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
bart = Student('Bart Simpson',59)
print bart.name
print bart.score

def print_score(std):
    print('%s:%s'%(std.name,std.score))

print_score(bart)
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' % (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        if self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson', 59)
print bart.print_score()
print bart.get_grade()


bart = Student('Bart Simpson',98)
print bart.score
bart.score = 59
print bart.score

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
bart = Student('Bart Simpson', 98)
print  bart.__name
class Student(object):
    pass

bart = Student()
print bart
print Student
bart.name = 'Bart Simpson'
print bart.name
bart = Student('Bart Simpson', 59)
print bart.print_score()
print bart.get_grade()



