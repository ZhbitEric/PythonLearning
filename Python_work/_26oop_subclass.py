# -- coding: utf-8 --
# 继承
# 子类调用方法时，总会先在子类中寻找方法，如果找不到，就会按继承父类的元组顺序去基类中找

class SchoolMember:
    '''Represents any school member.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

    # 两个父类都有此方法，会优先调用顺序在前的父类的方法
    def tell_1(self):
        print('SchoolMember tell')


class SchoolMember_2:
    def __init__(self, sex):
        self.sex = sex

    def tell_1(self):
        print('SchoolMember_2 tell')

    def tell_2(self):
        print('02 tell_2 {}'.format(self.sex))


class Teacher(SchoolMember, SchoolMember_2):
    '''Represents a teacher.'''

    def __init__(self, name, age, salary, sex):
        SchoolMember.__init__(self, name, age)
        SchoolMember_2.__init__(self, sex)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember, SchoolMember_2):

    def __init__(self, name, age, marks, sex):
        SchoolMember.__init__(self, name, age)
        SchoolMember_2.__init__(self, sex)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000, '男')
s = Student('Swaroop', 25, 75, '女')

print()

menber = [t, s]
for m in menber:
    m.tell()
    m.tell_1()
    m.tell_2()
