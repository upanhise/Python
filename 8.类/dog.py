# 类是定义一类对象的通用行为,也就是面向对象，类基本的作用是封装
# 创建和使用类


class Dog():
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        print(self.name.title() + " is  a " + str(self.age) + "-old Dog ")

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is  now sitting !")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over !")


# _init_(self) 构造函数会自动运行
# 根据类创建实例
# 调用方法
# 创建多个实例
dog_1 = Dog('white', 5)
dog_1.sit()
dog_1.roll_over()
dog_2 = Dog('Lucy', 8)
dog_3 = Dog('nancy', 3)

# 使用类和实例


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name


my_newcar = Car('audi', 'a4', 2019)
print(my_newcar.get_descriptive_name())

# 给属性指定默认值
# 指定默认值的属性不需要设置形参


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name.title())

    def get_odometer_reading(self):
        print("This car has " + str(self.odometer_reading) + " meter on it")

    def update_odometer_reading(self, odometer):
        self.odometer_reading = odometer

    def increment_odometer(self, odometer_numbel):
        self.odometer_reading += odometer_numbel


my_newcar = Car('audi', 'a4', 2019)
my_newcar.get_descriptive_name()
my_newcar.get_odometer_reading()

# 修改属性的值
# 1.直接修改属性的值
my_newcar.odometer_reading = 23
my_newcar.get_odometer_reading()

# 2.通过方法修改属性的值
# def update_odometer_reading(self, odometer):
#     self.odometer_reading = odometer

my_newcar.update_odometer_reading(50)
my_newcar.get_odometer_reading()

# 3.通过方法对属性的值进行递增
# def increment_odometer(self, odometer_numbel):
#     self.odometer_reading += odometer_numbel
my_newcar.increment_odometer(10)
my_newcar.get_odometer_reading()
my_newcar.increment_odometer(20)
my_newcar.get_odometer_reading()

# 子类的继承
# 一个类继承另一个类的是否，它将自动获得另一个类的所有属性和方法
# 原有的类被称为父类，而新类被称为子类
# 子类继承父类所有的属性和方法


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        """super()函数把子类和父类关联起来"""
        print("This is a electriccar !")


my_tesla = ElectricCar('tesla', 'model_s', 2019)
my_tesla.get_descriptive_name()
