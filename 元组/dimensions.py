# 元组是由不可修改的值组成的列表
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 同样的可以利用索引将元组中的元素进行调用
# 尝试修改元组中的值
# del dimensions[0](由于报错注释掉)
print(dimensions)
# 又或者尝试修改元组中的值
# dimensions[0] = 100(由于报错注释掉)
print(dimensions)
# 遍历元组中所有元素
values = []
for value in dimensions:
    print(value)
    values.append(value)
# 并创建一个列表输出打印出
print(values)


# 修改元组只需要对元组的变量赋值即可
dimensions = (400, 200)
print(dimensions)
