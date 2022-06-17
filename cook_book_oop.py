from pprint import pprint
import copy

class Dish():

    def __init__(self, dish_name = 'Unknown dish'):
        self.name = dish_name
        self.ingradients = {}

    def add_ingradient(self, name, quantity, measure):
        ingradient_amount = {}
        ingradient_amount['quantity'] = quantity
        ingradient_amount['measure'] = measure
        self.ingradients[name] = ingradient_amount

    def ingradients_to_list(self):
        ingradients_list = []
        for ingradient, amount in self.ingradients.items():
            ingradients_dict = {}
            ingradients_dict['ingredient_name'] = ingradient
            ingradients_dict['quantity'] = amount['quantity']
            ingradients_dict['measure'] = amount['measure']
            ingradients_list.append(ingradients_dict)
        return ingradients_list

    def __mul__(self, other: int):
        mult_dish = self
        for amount in mult_dish.ingradients.values():
            amount['quantity'] *= other
        return mult_dish

    def __imul__(self, other: int):
        mult_dish = self
        for amount in mult_dish.ingradients.values():
            amount['quantity'] *= other
        return mult_dish

    def shop_dict(self, count = 1, file_path = 'files\shop_list.txt'):
        shop_list = self * count
        with open(file_path, 'w', encoding='utf-8') as f_shop_list:
            f_shop_list.write(f'\tСПИСОК ИНГРЕДИЕНТОВ для закупки:\n\t{"-" * 33}\n')
        with open(file_path, 'a', encoding='utf-8') as f_shop_list:
            for ingradient, amount in shop_list.ingradients.items():
                str_to_file = f"\t{ingradient} - {amount['quantity']} {amount['measure']}\n"
                f_shop_list.write(str_to_file)
        return shop_list.ingradients

    def __add__(self, other):
        if isinstance(other, Dish):
            sum_dish = Dish('Sum_dishes')
            for ingradient, amount in self.ingradients.items():
                sum_dish.add_ingradient(ingradient, amount['quantity'], amount['measure'])
            for ingradient, amount in other.ingradients.items():
                if not ingradient in sum_dish.ingradients:
                    sum_dish.add_ingradient(ingradient, amount['quantity'], amount['measure'])
                else:
                    sum_dish.ingradients[ingradient]['quantity'] += amount['quantity']
        return sum_dish

    def __iadd__(self, other):
        if isinstance(other, Dish):
            sum_dish = Dish('Sum_dishes')
            for ingradient, amount in self.ingradients.items():
                sum_dish.add_ingradient(ingradient, amount['quantity'], amount['measure'])
            for ingradient, amount in other.ingradients.items():
                if not ingradient in sum_dish.ingradients:
                    sum_dish.add_ingradient(ingradient, amount['quantity'], amount['measure'])
                else:
                    sum_dish.ingradients[ingradient]['quantity'] += amount['quantity']
        return sum_dish

    def __str__(self):
        result_str = f'Для приготовления одной порции блюда "{self.name}" необходимо:\n'
        num = 0
        for ingradient, amount in self.ingradients.items():
            num += 1
            result_str += f"{num}. {ingradient}: {amount['quantity']} {amount['measure']}\n"
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

def cook_book(dishes_list):
    if not all([isinstance(member, Dish) for member in dishes_list]):
        return 'Ошибка: не все элементы списка принадлежат class Dish'
    cook_book = {}
    for dish in dishes_list:
        cook_book[dish.name] = dish.ingradients_to_list()
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
