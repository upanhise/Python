cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# for语句的格式问题，注意缩进
# 条件测试
# python 是个根据条件测试的值为true还是false来决定是否执行if后面的语句
# python在考虑值是否相等时，会检查大小写，如何检查是否相等时不用考虑大小写得使用lower() ，upper()和title()方法
# 用"=="来询问是否相等，用"!="来询问是否不相等，如果回答是true则接着执行下面的语句
age = 18
if age == 18:
    print(True)
else:
    print(False)

age = 18
if age != 20:
    print(True)
    print("That is not the correct answer, Please try again !")
else:
    print(False)

# 检查多个条件,用and链接两个删选条件
age_0 = 22
age_1 = 38
if age_0 >= 22 and age_1 <= 38:
    print(True)
else:
    print(False)
# 检查多个条件，用or链接两个删选条件
if age_0 >= 22 or age_1 != 38:
    print(True)
else:
    print(False)

# 检查特定值是否包含在列表中
# 要判断是否包含在列表中，可使用关键字in(if '字符串' in list[])
request_toppings = ['mushrooms', 'onions', 'pineapple']
if 'onions' in request_toppings:
    print(True)
else:
    print(False)
if 'beef' in request_toppings:
    print(True)
else:
    print(False)
# 要判断是否不包含在列表中，可使用关键字in(if '字符串' not in list[])
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 布尔表达式
# 布尔表达式的结果要么是True，要么是False，常用于记录条件
game_active = True
can_edit = False

# if的高级形式，if elif else
age = 20
if age < 15:
    print("Your admission cost is $0 ")
elif age < 30:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")
# 视条件可采用多个elif 结构
# 测试多个条件,采用一系列的if语句，各个if语句之间相互独立
request_toppings = ['mushroonms', 'extra cheese']
for request in request_toppings:
    if request in request_toppings:
        print("adding " + request.title())

# 使用if语句处理列表

request_toppings = ['mushrooms', 'green papers', 'extra cheese']
for request in request_toppings:
    print("Adding " + request.title() + ".")
print("\nFinished making your pizza")

# 确认列表为空,用if list[]: 判断列表元素是否为空。
request_toppings = ['mushrooms', 'green papers', 'extra cheese']
if request_toppings:
    for request in request_toppings:
        print("Adding " + request.title() + ".")
else:
    print("\nAre you sure want a plain pizza ?")
print("\nFinished making your pizza.")
