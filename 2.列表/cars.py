# 列表排列
cars = ['bew', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# 通过sort方法对列表进行永久排列
# 现在cars是默认按照字母a，b，c，顺序排列
# 且sort方法的顺序是可以改变的只需要对sort方法进行设置
cars_2 = ['bew', 'audi', 'toyota', 'subaru']
cars_2.sort(reverse=True)
print(cars_2)
# 设定reverse=True便可以将sort以字母顺序相反的顺序排列
# 利用sorted()方法对列表进行临时排列
motocycles = ['honda', 'yamaha', 'suzuki', 'ducaki']
print("Here is the original list : ")
print(motocycles)
print("Here is the sorted list : ")
print(sorted(motocycles))
print("/nHere is the original list : ")
print(motocycles)
# 将原始列表和sorted()方法排列后的列表打印出来进行比较
# 同样的也可以通过调整参数reverse=True对sorted()进行设置让列表临时按照字母相反的顺序排列
# reverse()方法可以倒着打印列表,反转列表的打印顺序，永久性的修改列表排列顺序，但是也可以随时恢复，只需要再执行一次就可以
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# len()方法可以确认列表的长度
numble = len(cars)
print(numble)
