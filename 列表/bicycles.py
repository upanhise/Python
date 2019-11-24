# 列表是由一系列按特定顺序排列的元素组成
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 访问列表中的元素
# 列表中的索引是从0开始而不是从1开始
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3])
# 可以使用特殊语法，通过指定索引为-1，可以返回最后一个元素
print(bicycles[-1].title())
# 使用列表中的各个值创建消息
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
# 修改，添加和删除元素
motorcycles = ['honad', 'yamaha', 'suzuki']
print(motorcycles[0].title())
motorcycles[0] = 'ducati'
print(motorcycles[0].title())
# 在列表的末尾添加元素
motorcycles.append('anki')
print(motorcycles)
# 也可以利用append()创建列表
Y = []
Y.append('U')
Y.append('O')
Y.append('T')
print(Y)
# 列表中插入元素
motorcycles.insert(0, 'wall')
print(motorcycles)
# 列表删除元素
# 利用 del 删除元素，在知道列表中元素的索引的元素可以利用del 定位元素进行删除
del motorcycles[0]
print(motorcycles)
# 利用pop() 删除元素，方法pop()可以弹出列表末尾的元素，相当于弹出栈顶的元素，且能接着使用该元素
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)
# pop()也能在知道索引的情况下弹出列表任意位置处的元素
popped_motorcycles = motorcycles.pop(0)
print(popped_motorcycles)
print(motorcycles)
# 如果知晓列表中Value，则可以利用remove(Value)方法进行删除列表中的元素
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("The reason why i don't want " + too_expensive + " is the price")
# 如果列表中存在多个相同的Value，则可以根据循环方式判断是否删除所有相同的值
