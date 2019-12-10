#  使用列表的一部分，pyhon的切片操作
players = ['charles', 'martina', 'michael', 'florence', 'eil']
print(players[0:3])
# 将原来的列表进行切片，利用这种方法可以生成列表的任意子集
# 如果没有指定第一个索引，那么默认从开头
print(players[:4])
# 同样的如果没有指定第二个索引，那么默认到最后一个元素
print(players[2:])
# 还可以指定负数来从末尾开始生成子集
print(players[-2:])

# 遍历切片
# 利用for循环来遍历切片
for player in players[1:3]:
    print(player.title())

# 复制列表
# 可以通过省略起始索引和终止索引来复制整个列表
foods = ['pizza', 'falafel', 'carrot cake']
My_foods = []
for food in foods[:]:
    My_foods.append(food)
print(My_foods)

# 或者这样写
My_friend_foods = foods[:]
print(My_friend_foods)
