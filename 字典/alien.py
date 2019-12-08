# 字典，用来存储一系列的信息和属性
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# 字典的格式要清楚，{'属性表头'： '属性值'},字典是系列-键值对
# 在字典里添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 修改字典中的值，依旧是更新字典键值对
alien_0['color'] = 'yellow'
print(alien_0)
# 删除字典中的键值对
del alien_0['color']
print(alien_0)
# 字典也可以存储由类似对象的集合
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("jen favorite language is " +
      favorite_language['jen'].title() +
      ".")

# 遍历字典
# 遍历字典中所有的键对，用 for key,value in dict.items():
user_0 = {
    'username': 'CheerBob',
    'first_name': 'Cheer',
    'last_name': 'Bob',
}
for key, value in user_0.items():
    print("\nkey" + ":\t" + key)
    print("value" + ":\t" + value)

# 遍历字典中所有的键
# 对于遍历字典中所有的键，用方法Key()会很有效
print("All the key ：")
for name in user_0.keys():
    print("\t\t" + name)
# 在访问键的循环中还可以使用循环的键来访问与之相关联的值
friends = ['jen', 'sarah']
for key, value in favorite_language.items():
    print(key.title())
    if key in friends:
        print("Hi! My best friend " +
              key.title() + ". Your favorite language is " +
              value.title())
        print("\n")

# 按顺序遍历字典中所有的键 (sorted()方法)
for key in sorted(favorite_language.keys()):
    print("\t\t" + key.title())
print("\n")
# 遍历字典中所有的值
for value in favorite_language.values():
    print("\t\t" + value.title())
print("\n")
# 但是这样输出的值包含大量相同的值，可以采用set(集合)的方法唯一化
for value in set(favorite_language.values()):
    print("\t\t" + value.title())
