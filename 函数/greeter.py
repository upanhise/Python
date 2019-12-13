# 函数是带有名字的代码块，在执行同一任务时，无需反复编写代码
def greet_user():
    """显示简单的问候语"""
# 其中 """ """  为文档字符串，用来描述函数作用
    print("Hello !")


greet_user()

# 向函数传递信息，在括号中传递


def greet_user(username):
    print("Hello ,My best friend " + username.title())


greet_user('bob')

# 实参和形参
# 在上面那个函数中，username是形参，指代需要输入的类型 ，而'Bob',是实参，指代实际的人名
# 实参的传递，向函数传递给实参有很多种方式，可使用位置实参，这要求实参和形参的位置报错一致
# 也可以使用关键字实参，其中每个实参都由变量名和值组成，还可以使用列表和字典


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')

# 调用函数多次
describe_pet('cat', 'Bob')

# 在引用函数进行调用的是否，使用位置实参需要保证形参和实参位置一致
# 关键字实参，可以不考虑位置
describe_pet(animal_type='dog', pet_name='marry')

# 默认值
# 编写程序时，可以给形参指定默认值，在调用函数中给形参提供实参时，python将使用实参值，否则将使用形参的默认值
# 且默认值放在后面  ！！！！！(如果不放后面记得关键字指定实参！！！)


def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 这个是否不用关键字指定也可，但是如果参数超过三个还是需要关键字指定实参或者位置实参
describe_pet('bob')
describe_pet(pet_name='Hellr')

# 返回值


def get_formatted_name(first_name, last_name):
    full_name = first_name.title() + "  " + last_name.upper()
    return full_name


muscian = get_formatted_name('jimi', 'hendrix')
print(muscian)

# 让实参变成可选的


def get_formatted_name(first_name,  last_name, middle_name=''):
    if middle_name:
        full_name = first_name.title() + " " + middle_name.lower() + \
            " " + last_name.lower()
    else:
        full_name = first_name.title() + " " + last_name.lower()
    return full_name


muscian = get_formatted_name('jimi', 'hendrix')
print(muscian)

muscian = get_formatted_name('john', 'hooker', 'lee')
print(muscian)

# 返回字典


def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


muscian = build_person('jimi', 'hendrix')
print(muscian)


def build_person(first_name, last_name, age=' '):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


muscian = build_person('jimi', 'hendrix', age=28)
print(muscian)

# 结合使用函数和while,其中while可能导致无限循环们需要bereak 指定停止条件


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name :")
    print("(Enter 'q' to quit the program)")
    first_name = input("Enter your first name\n")
    if first_name.lower() == 'q':
        break
    last_name = input("Enter your last name")
    if last_name.lower() == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print(formatted_name)

# 传递列表
# 括号里的能够给与列表


def greet_users(names):
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)


greet_users(['hannah', 'ty', 'margot'])

# 在函数中修改列表


def unprint_designs(input_designs, completed_models):
    while input_designs:
        current_designs = input_designs.pop()
        print("Printing model : " + current_designs)
        completed_models.append(current_designs)


def show_completed_designs(completed_models):
    print("\nThe following models have been printed ")
    for design in completed_models:
        print("\t\t\t\t\t\t" + design)


input_designs = []
completed_models = []
active = True
while active:
    print("Enter 'q' to quit")
    input_design = input("Please enter the design ！\n")
    if input_design != 'q':
        input_designs.append(input_design)
    else:
        active = False
if input_designs:
    print(input_designs)
    unprint_designs(input_designs, completed_models)
    show_completed_designs(completed_models)


# 禁止函数修改列表
# 有时候需要保留修改前的列表，可创造列表的副本进行操作
# function(list_name[:])

# 传递任意数量的实参
# *topping ；利用*dime 创建意格元组，将输入的实参组成一个元组
def making_pizza(*toppings):
    print("\n Makeing a pizza with following toppings : ")
    for topping in toppings:
        print("- " + topping)


making_pizza('pepperoni')
making_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置参数和任意数量参数


def make_pizza(size, color, *toppings):
    print("Making a " + str(size) + "-size   " +
          color + " pizza with following toppings ")
    for topping in toppings:
        print("- " + topping)


make_pizza(18, 'red', 'pepperoni')
make_pizza(28, 'green', 'mushrooms', 'green eppers', 'extra cheese')

# 使用任意数量的关键字实参


def make_pizza_2(size, color, **toppings):
    print("Making a " + str(size) + "-size  " +
          color + " pizza with following toppings ")
    for key, topping in toppings.items():
        print("- \t\t\t\t\t\t\t\t" + topping)


make_pizza_2(color='green', size=39, topping_1='mushrooms',
             topping_2='extra cheese')
