from pprint import pprint
import sys

class Dish():

    def __init__(self, dish_name = 'Unknown dish'):
        self.name = dish_name
        self.ingradients = []

    def add_ingradient(self, name, quantity, measure):
        ingradient = {}
        ingradient['ingredient_name'] = name
        ingradient['quantity'] = quantity
        ingradient['measure'] = measure
        self.ingradients.append(ingradient)

    def shop_dict(self, count = 1, file_path = 'files\shop_list.txt'):
        shop_dict = {}
        for ingradient in self.ingradients:
            # if ingradient['ingredient_name'] in shop_dict:
            #     shop_dict[ingradient['ingredient_name']]['quantity'] += ingradient['quantity'] * count
            # else:
            amount_ingradient = {}
            amount_ingradient['measure'] = ingradient['measure']
            amount_ingradient['quantity'] = ingradient['quantity'] * count
            shop_dict[ingradient['ingredient_name']] = amount_ingradient
        with open(file_path, 'w', encoding='utf-8') as f_shop_list:
            f_shop_list.write(f'\tСПИСОК ИНГРЕДИЕНТОВ для закупки:\n\t{"-" * 33}\n')
        with open(file_path, 'a', encoding='utf-8') as f_shop_list:
            for ingradient, amount in shop_dict.items():
                str_to_file = f"\t{ingradient} - {amount['quantity']} {amount['measure']}\n"
                f_shop_list.write(str_to_file)
        return shop_dict

    def __contains__(self, item):
        for ingradient in self.ingradients:
            if ingradient['ingredient_name'] == item:
                return True
        return False

    def __add__(self, other):
        if isinstance(other, Dish):
            sum_dish = Dish('Sum_dishes')
            for ingradient in self.ingradients:
                sum_dish.add_ingradient(ingradient['ingredient_name'], ingradient['quantity'], ingradient['measure'])
            for ingradient in other.ingradients:
                if not ingradient['ingredient_name'] in sum_dish:
                    sum_dish.add_ingradient(ingradient['ingredient_name'], ingradient['quantity'], ingradient['measure'])
                else:
                    for ingradient2 in sum_dish.ingradients:
                        if ingradient['ingredient_name'] == ingradient2['ingredient_name']:
                            ingradient2['quantity'] += ingradient['quantity']
        return sum_dish

    def __iadd__(self, other):
        if isinstance(other, Dish):
            sum_dish = Dish(self.name)
            for ingradient in self.ingradients:
                sum_dish.add_ingradient(ingradient['ingredient_name'], ingradient['quantity'], ingradient['measure'])
            for ingradient in other.ingradients:
                if not ingradient['ingredient_name'] in sum_dish:
                    sum_dish.add_ingradient(ingradient['ingredient_name'], ingradient['quantity'], ingradient['measure'])
                else:
                    for ingradient2 in sum_dish.ingradients:
                        if ingradient['ingredient_name'] == ingradient2['ingredient_name']:
                            ingradient2['quantity'] += ingradient['quantity']
        return sum_dish

    def __str__(self):
        result_str = self.name + '\n'
        result_str += f'{self.ingradients}'
        return result_str

def dishes_list_from_file(file_path):
    dishes_list = []
    with open(file_path, encoding='utf-8-sig') as f_cook_book:
        for line in f_cook_book:
            if not line.strip():
                return
            new_dish = Dish(line.strip())
            quantity_ingradients = int(f_cook_book.readline().strip())
            for item in range(quantity_ingradients):
                ingradient_list = f_cook_book.readline().strip().split(' | ')
                new_dish.add_ingradient(ingradient_list[0], int(ingradient_list[1]), ingradient_list[2])
            f_cook_book.readline()
            dishes_list.append(new_dish)
    return dishes_list

def cook_book(dihes_list):
    if not all([isinstance(member, Dish) for member in dishes_list]):
        return 'Ошибка: не все элементы списка принадлежат class Dish'
    cook_book = {}
    for dish in dihes_list:
        cook_book[dish.name] = dish.ingradients
    return cook_book

def returned_dish(dishes_list, name):
    if not all([isinstance(member, Dish) for member in dishes_list]):
        return 'Ошибка: не все элементы списка принадлежат class Dish'
    for dish in dishes_list:
        if dish.name == name:
            return dish
    return Dish()

def get_shop_list(dishes_list, list_of_dishes_names, count_persons = 1):
    if not all([isinstance(member, Dish) for member in dishes_list]):
        return 'Ошибка: не все элементы списка принадлежат class Dish'
    sum_dish = Dish()
    for dish_name in list_of_dishes_names:
        sum_dish += returned_dish(dishes_list, dish_name)
    return sum_dish.shop_dict(count_persons)

file_path = 'files\cook_book.txt'
dishes_list = dishes_list_from_file(file_path)
print("Задача № 1 формирования словаря cook_book из файла:\n")
print('cook_book =')
pprint(cook_book(dishes_list))
print("=" * 60)
print("\nЗадача № 2 формирования списка закупок на количество клиентов:\n")
list_of_dishes_names =  ['Фахитос', 'Омлет']
count_persons = 5
pprint(get_shop_list(dishes_list, list_of_dishes_names, count_persons))
print("=" * 60)
