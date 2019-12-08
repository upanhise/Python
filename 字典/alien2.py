# 将一系列字典存储在列表中，或者将列表作为值存储在字典中，这一过程被称为嵌套
alien_0 = {'color': 'bule', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 50}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 在字典中存储列表
# 存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# 概述所点的披萨
print("Your oedered a " + pizza['crust'] +
      "-crust pizza" + " with the following toppings :")
for topping in pizza['toppings']:
    print("\t\t\t" + topping)

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie':  {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }

}
for username, user_info in users.items():
    print("\nUsername : " + username)
    full_name = user_info['first'].title() + user_info['last'].title()
    location = user_info['location']
    print("Full_name : " + full_name)
    print("location : " + location)
