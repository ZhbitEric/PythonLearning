# -- coding: utf-8 --
# 初始化函数 __init__

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('hi,my name is', self.name)


p = Person('xrd')
p.say_hi()


class Robot:
    # A class variable,类变量 全部实例共享
    population = 0
    # 加双下划线 则变成私有变量
    # __population = 0

    # name是对象变量，每个对象自己享有
    def __init__(self, name):
        self.name = name
        print('(initializing {})'.format(self.name))

        Robot.population += 1

    def die(self):
        print('{} is being destroyed!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            # Robot.population 等价于 self.__class__.population
            print('there are still {:d} robots working.'.format(Robot.population))
            print('also can use {:d}.'.format(self.__class__.population))

    def say_hi(self):
        """Prints the current population."""
        print('Greetings,my masters call me {}.'.format(self.name))

    # 属于类的方法 所以实例对象共享
    @classmethod
    def how_many(cls):
        print('we have {:d} robots.'.format(cls.population))


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
print(Robot.say_hi.__doc__)

