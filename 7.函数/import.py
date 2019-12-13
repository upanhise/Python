# 将函数存储在模块
# 例如
from pizza import *
import pizza as piz
from pizza import make_pizza as mp
from pizza import make_pizza
import pizza
pizza.make_pizza(16, 'green', 'pepperoni')

# 也可以导入特定的函数
make_pizza(28, 'red', 'pepperoni')

# 如果名称过长或者重名，可以使用as 方法给指定函数指定别名
mp(38, 'red', 'pepperoni')

# 使用as方法给模块指定别名
piz.make_pizza(38, 'green', 'pepperoni')

# 导入模块中所有函数，可以使用 from model_name import *
make_pizza(28, 'red', 'pepperoni')

# 函数编写指南
# first 给函数指定描述性名称
# second 每个函数应该包含简要的阐述功能的注释
# third 给形参设定默认值时，等号两边不要有空格
