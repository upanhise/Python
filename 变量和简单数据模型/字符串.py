name = ("ada lovelace")
# 赋予name的变量调用title方法让名字大写
print(name.title())
# 调用upper和lower方法对字符串改为全部大写或者全部小写
print(name.upper())
print(name.lower())
# 字符串合并
first_name = ("ada")
last_name = ("lovelace")
full_name = (first_name.title() + "      " + last_name + "\t")
print(first_name.title() + "      " + last_name)
# 换行符和制表符
print("\t" + first_name.title() + "      " + last_name)
print(first_name.title() + "\n" + "\t" + last_name)
# rstrip 删除字符串末尾的空白（暂时消除空格，下次访问依旧存在空格）
# lstrip 删除字符串开头的空白
# strip  删除字符串两端的空白
print(full_name.rstrip())
print(full_name.lstrip())
print(full_name.strip())
# 只有删除后更新字符串才能永久删除
full_name = full_name.rstrip()
print(full_name.title())
