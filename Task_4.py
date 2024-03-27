# 1. Создайте функцию route_info, которой будет передаваться словарь.
# 2. Если в словаре есть ключ distance и его значение целое число, верните строку "Distance to your destination is <distance>"
# 3. Иначе, если в словаре есть ключи speed и time, верните строку "Distance to your destination is <speed * time>"
# 4. Иначе верните строку "No distance info is available"
# 5. Вызовите функцию несколько раз с разными аргументами

my_list = {
    'distance': 12,
  
}
my_list_two = {
    'speed': 10,
    'time': 13,
}
my_list_three = {
    'name': 'Arpi',
    'age': 29,
}
def route_info(my_list_key):
    if 'distance' in my_list_key and isinstance(my_list_key['distance'], int):
        return f"Distance to your destination is {my_list_key['distance']}"
    elif "speed" in my_list_key and 'time' in my_list_key:
        distance = my_list_key['speed'] * my_list_key['time']
        return f"Distance to your destination is {distance}"
    else:
        return "No distance info is available"
        
    
print(route_info(my_list))
print(route_info(my_list_two))
print(route_info(my_list_three))