# 数字列表
# 利用range()让你能够轻松生成数字列表
# range()方法用法range(2,11,2),输出的数字是以2开始，等差为2，直到达到或者超过11为止
for value in range(1, 5):
    print("\t" + str(value))
# 在这里空格制表符的时候  can only concatenate str to str， 因此Str()转变为字符
# 将range()方法输出的数字用list()方法生成列表
numbles = list(range(1, 5))
print(numbles)

squars = []
for value in range(1, 8, 1):
    squar = value ** 2
    squars.append(squar)
print(squars)

# 为了代码简洁，直接利用 squars.append(value ** 2)

# 对数字列表进行统计计算最大值，最小值，总和
digits = range(1, 10)
another_digits = []
for digit in digits:
    print(digit)
    another_digits.append(digit)
print(another_digits)
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
# 列表解析用for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value ** 2 for value in range(2, 8, 2)]
print(squares)

# 计算1-1000的总和
numble_sum = [sum for value in range(1, 1000)]
print(numble_sum)

# 奇数
odd_numble = []
for numble in range(1, 15, 2):
    print(numble)
    odd_numble.append(numble)
print(odd_numble)

# 将3-30内的能够被3整除的数字挑选出并用for循环打印出来
list_3 = []
for numble in range(3, 30, 3):
    print(numble)
