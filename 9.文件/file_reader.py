# 打开指定目录下的 文件.txt
with open('G:\Demos\Python\9.文件和异常\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# 由于read()方法在阅读文件的时候最后会返回一个空字符串，显示出来就是空行
# 使用strip()方法删除空行
# 逐行读取
filename = 'G:\Demos\Python\9.文件和异常\pi_digits.txt'

with open(filename) as file_object:
    """逐行读取"""
    for line in file_object:
        print(line)

# 创建一个包含文件各行内容的列表
filename = 'G:\Demos\Python\9.文件和异常\pi_digits.txt'
N = []
pi_string = ''
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        N.append(line.strip())
        pi_string += line.strip()
        print(line.strip())
    print(N)
    print(pi_string)
    print("字符串的长度为： " + str(len(pi_string)))
# 逐行读取文件并输出,将各行组成一个列表输出
# 输出pi_string 的字符串和字符长度

# 写入文件
filename_2 = 'G:\Demos\Python\9.文件和异常\programming.txt'
with open(filename_2, 'w') as file_object:
    file_object.write("I love Programming\n")

# 'w' 表示以write模式处理文件
# 'r' 表示以read模式处理文件
# 'r+' 表示以write和read模式处理文件
# 'a' 表示以附加模式处理文件

#  写入多行,用换行符\n 让字符独占一行
    file_object.write("I Love Creat New Games !\n")
    file_object.write("I Love Creat New Games !")

# 附加到文件
# 如果要给文件添加内容，而不是覆盖原有内容，可以附加模式打开文件
with open(filename_2, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser. \n")
# 'a'模式下写入的行会添加到文件的末尾
#  原来的文件还在
