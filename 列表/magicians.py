# 利用for循环遍历列表
magicians = ('alice', 'david', 'carolina')
for magician in magicians:
    # for 循环的用法是for Value in Values：
    print(magician)
# for 循环接下来的是需要进行的操作
# for循环对于列表中的每个元素，都要执行循环指定的步骤，不管列表中包括多少个元素
    print(magician.title() + ", that was a great trick")
# 可以对循环部进行更多的操作，例如每执行一次循环就打印一句赞赏的语句或者是期待你的下次表演
    print("I can't wait to see your next trick, " + magician.title() + "\n")
# 在语句的后面加入\n进行换行
# for循环要注意缩进，由于python是根据代码行缩进来判断代码间的关系
# 1.避免缩进错误
# 2.忘记缩进
# 3.不必要的缩进
# 4.for循环注意格式正确

# pizza 实例
pizzas = ['pizza_a', 'pizza_b', 'pizza_c']
for pizza in pizzas:
    print(pizza.title() + "I like pepperoni pizza")
print("pizza_a is big, pizza_b is expensive, pizza_c is cheap, I really like pizza")

# animals 实例
animals = ['dog', 'cat', 'duck']
for animal in animals:
    print("A " + animal + " would make a great pet")
print("Any of these animals would make a great pet " + "!")
