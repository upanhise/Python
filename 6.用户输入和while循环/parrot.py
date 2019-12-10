# 函数input()让用户可以输入一些信息，等待python存储后方便使用
message = input("Tell me something , and I will repeat it to you : ")
print(message)

# 在提示用户输入的是否可以提示用户输入的数据类型
name = input("Please enter your name : ")
print("Hello ! " + name)

# 用 += 创建多行字符串
prompt = "If you tell us who you are ,we can personalize the message you see ."
prompt += "\nWhat is your first name ?"
name = input(prompt)
print("\nHello , " + name + "!")

# 使用int()获取数字输入
age = input("How old are you ?")
age = int(age)
# 指明年龄的类型是数值，将str()转化为int()
print(age)

height = input("How tall are you , in inches?")
height = int(height)
if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older")

# 求模运算符 % 是一个很有用的工具，他将两个数相除并返回余数
a = 4 % 3
a = float(a)
print(a)

# 利用求模运算符判断是否余数为0，偶数整除的话返回余数为0
numble = input("Enter a numble ,and I will tell you if it is even or odd:  ")
numble = int(numble)
if numble % 2 == 0:
    print("The numble is even")
else:
    print("The numble is odd")

# while循环
couning_numble = 1
while couning_numble <= 5:
    print(couning_numble)
    couning_numble += 1

# 让用户选择何时退出
# 定义一个退出值，当用户输入的不是这个值，程序接着运行
prompt = "\nTell me something and i will repeat it back to you "
prompt = "\nEnter 'quit' to end the program"
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
# 发现quit输入的是否并没有正确被停止程序

# 接下来进行修改
prompt = "\nTell me something and i will repeat it back to you "
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != 'quit':
    message = input(prompt)
# 以上是判断输入的条件，只要控制输入quit后停止输出就可以
    if message != 'quit':
        print(message)
    else:
        # 使用break立刻退出while循环
        break

# 使用标志
prompt = "\nTell me something and i will repeat it back to you "
prompt += "\nEnter 'quit' to end the program"
message = ""
active = True
# 其中active 为程序是否执行的标志
while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        active = False

# 在while 中使用break 和 coutinue 控制程序运行
curent_numble = 0
while curent_numble < 10:
    curent_numble += 1
    if curent_numble % 2 == 0:
        continue
# coutinue 表示符合条件的话回到while接着执行
    else:
        print(curent_numble)

# 使用while循环处理列表和字典
uncomfirme_users = ['alice', 'brain', 'candace']
comfirme_users = []
while uncomfirme_users:
    comfirme_user = uncomfirme_users.pop()
    print("Verifying user : " + comfirme_user.title())
    comfirme_users.append(comfirme_user)
print("\nThe following users have been comfirmed :")
for user in comfirme_users:
    print("\t\t\t" + user.title())

# 删除包含特定值的所有列表元素
# 先用for 循环去筛选
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
for pet in pets:
    if pet == 'cat':
        pets.remove(pet)
print(pets)
# 要注意 pop只是弹出需要的列表元素，原列表并不会发生改变
# 用while语法筛选
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    # 与for循环不同，while循环将筛选和循环一起完成 ，取消中间变量pet，更加简洁
    pets.remove('cat')
print(pets)

# 使用用户输入来填充字典
responds = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name ?")
    respond = input("Which mountain would you like to cilmb someday")
    responds[name] = respond
    repeat = input("\nWould you like to lat another person respond?(Yes/No) ")
    repeat = repeat.title()
    if repeat == 'No':
        polling_active = False
    print("\n----Poll Resule----")
    print(name + " Would like to climb " + respond + ".")
