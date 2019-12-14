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
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-Kwh battery")


my_tesla = ElectricCar('tesla', 'model_s', 2019)
my_tesla.get_descriptive_name()

# 给子类定义属性和方法
# 让子类继承父类后，可以添加区分子类和父类的新属性和方法
# 添加电动汽车特有属性电瓶 self.battery_size = 70
# 添加电动汽车电瓶的描述方法 describe_battery

my_tesla.describe_battery()

# 重写父类的方法
# 可以通过在子类定义一个父类同名的方法对父类方法进行更新
# def fill_gas_tank(self):
#  """电瓶汽车没有油箱"""
#     print("This car doesn't need a gas tank !")

# 将实例用作属性


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=180,):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶的消息"""
        print("This has a " + str(self.battery_size) + "-Kwh battary")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 60:
            range = 240
            """局部变量range"""
        if self.battery_size == 180:
            range = 600
        print("This car can go approximately " +
              str(range) + " miles on a full charge")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        """创建一个self.battery_size属性,每次运行都将要创建一个对应的battery()实例"""
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model_s', 2019)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 导入类
# Python 标准库
# 类编码风格
# 1.类命名用驼峰命名法，类名中每个单词首字母大写，不使用下划线，实例名和模块名采用小写格式，并在单词间加上下划线
# 2.在类中，可使用一个空行分隔方法，在模块中，可使用两个空行来分隔类
# 3.先编写导入标准库模块的import语句，再添加一个空行，然后再编写导入自己编写模块的import语句
