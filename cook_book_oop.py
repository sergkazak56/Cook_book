from pprint import pprint
import os
import copy
import json
import csv

# Объектно-ориентированный метод

class Dish():
    '''
    Класс Dish (блюдо)
    name -  наименование блюда;
    ingradients - словарь с инградиентами и их количеством для приготовления блюда
    '''
    def __init__(self, dish_name = 'Unknown dish'):
        self.name = dish_name
        self.ingradients = {}

    def add_ingradient(self, name, quantity, measure):
        '''
        :param name - наименование ингредиента блюда;
        :param quantity - количество ингредиента блюда;
        :param measure - единица измерения ингредиента блюда;
        Метод добавляет инградиент в словарь инградиентов блюда
        '''
        ingradient_amount = {}
        ingradient_amount['quantity'] = quantity
        ingradient_amount['measure'] = measure
        self.ingradients[name] = ingradient_amount

    def ingradients_to_list(self):
        '''
        :return: ingradients_list - преобразованный в список словарь инградиетов (ingradients) блюда;
        Метод преобразует словарь инградиентов в список словарей.
        '''
        ingradients_list = []
        for ingradient, amount in self.ingradients.items():
            ingradients_dict = {}
            ingradients_dict['ingredient_name'] = ingradient
            ingradients_dict['quantity'] = amount['quantity']
            ingradients_dict['measure'] = amount['measure']
            ingradients_list.append(ingradients_dict)
        return ingradients_list

    # Переопределенный метод для умножения экземпляров класса Dish на число:
    def __mul__(self, number: float):
        '''
        :param number - значение числа типа float;
        :return: mult_dish - экземпляр класса Dish умноженное на number;
        Метод умножает количество ингредиентов блюда на число number
        '''
        mult_dish = self
        for amount in mult_dish.ingradients.values():
            amount['quantity'] *= number
        return mult_dish

    # Переопределенный метод для умножения экземпляров класса Dish на число:
    def __imul__(self, number: float):
        '''
        :param number - значение числа типа float;
        :return: mult_dish - экземпляр класса Dish умноженное на number;
        Метод умножает количество ингредиентов блюда на число number
        '''
        mult_dish = self
        for amount in mult_dish.ingradients.values():
            amount['quantity'] *= number
        return mult_dish

    def shop_dict(self, count = 1, file_path = 'files\shop_list.txt'):
        '''
        :param count - количество блюд, для которого формируется лист покупок (shop_list) (default = 1);
        :param file_path - путь выводного файла для записи shop_list (default = 'files\shop_list.txt');
        :return: shop_list.ingradients - словарь с необходимыми ингредиентами и их количеством;
        Метод формирует словарь-список ингредиентов, необходимых к закупке, а также файл с таким списком
        '''
        shop_list = self * count
        if os.path.exists(os.path.dirname(file_path)):
            with open(file_path, 'w', encoding='utf-8') as f_shop_list:
                f_shop_list.write(f'\tСПИСОК ИНГРЕДИЕНТОВ для закупки:\n\t{"-" * 33}\n')
            with open(file_path, 'a', encoding='utf-8') as f_shop_list:
                for ingradient, amount in shop_list.ingradients.items():
                    str_to_file = f"\t{ingradient} - {amount['quantity']} {amount['measure']}\n"
                    f_shop_list.write(str_to_file)
        return shop_list.ingradients

    # Переопределенный метод для сложения экземпляров класса Dish:
    def __add__(self, other):
        '''
        :param other - представитель класса Dish, с которым производится сложение;
        :return: sum_dish - экземпляр класса Dish, полученный в результате сложения двух его представителей;
        Метод объединяет словари ingradients обеих блюд, а у одинаковых ингредиентов
        складывает их количество
        '''
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

    # Переопределенный метод для сложения экземпляров класса Dish:
    def __iadd__(self, other):
        '''
        :param other - представитель класса Dish, с которым производится сложение;
        :return: sum_dish - экземпляр класса Dish, полученный в результате сложения двух его представителей;
        Метод объединяет словари ingradients обеих блюд, а у одинаковых ингредиентов
        складывает их количество
        '''
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

    # Переопределенный метод для вывода экземпляров класса Lecturer:
    def __str__(self):
        result_str = f'Для приготовления одной порции блюда "{self.name}" необходимо:\n'
        num = 0
        for ingradient, amount in self.ingradients.items():
            num += 1
            result_str += f"{num}. {ingradient}: {amount['quantity']} {amount['measure']}\n"
        return result_str

def dishes_list_from_file(file_path):
    '''
    :param file_path - путь к файлу cook_book.txt, где находятся структурированные данные по блюдам;
    :return: dishes_list - список блюд (экземпляров class Dish);
    Функция считывает файл  cook_book.txt и создает из него список блюд (экземпляров class Dish)
    '''
    if not os.path.exists(file_path):
        print('Ошибка: неверно задан путь к файлу cook_book.txt')
        return False
    dishes_list = []
    with open(file_path, encoding='utf-8-sig') as f_cook_book:
        for line in f_cook_book:
            if not line.strip():
                return
            new_dish = Dish(line.strip())
            quantity_ingradients = int(f_cook_book.readline().strip())
            for item in range(quantity_ingradients):
                ingradient_list = f_cook_book.readline().strip().split(' | ')
                new_dish.add_ingradient(ingradient_list[0], float(ingradient_list[1]), ingradient_list[2])
            f_cook_book.readline()
            dishes_list.append(new_dish)
    return dishes_list

def get_cook_book(dishes_list):
    '''
    :param dishes_list - список блюд (экземпляров class Dish);
    :return: cook_book - поваренная книга в виде словаря определенного формата;
    Функция формирует словарь cook_book из списока блюд (экземпляров class Dish)
    '''
    if not all([isinstance(member, Dish) for member in dishes_list]):
        return 'Ошибка: не все элементы списка принадлежат class Dish'
    cook_book = {}
    for dish in dishes_list:
        cook_book[dish.name] = dish.ingradients_to_list()
    make_json_cook_book({'Поваренная книга':cook_book})
    return cook_book

def returned_dish(dishes_list, name):
    '''
    :param dishes_list - список всех блюд (экземпляров class Dish);
    :param name - наименование блюда;
    :return: dish - экземпляр class Dish, наименование которого соответствует name;
    Функция находит блюдо среди списка экземпляров class Dish по имени. Если такого блюда нет,
    то возвращает пустой эземпляр class Dish
    '''
    for dish in dishes_list:
        if dish.name == name:
            return dish
    return Dish()

def get_shop_list(dishes_list, list_of_dishes_names, count_persons = 1):
    '''
    :param dishes_list - список всех блюд (экземпляров class Dish);
    :param list_of_dishes_names - список наименований выбранных блюд;
    :param count_persons - количество человек, для которых надо произвести расчет количества ингредиентов;
    :return: словарь-список закупок;
    Функция формирует словарь-список закупок, исходя из количества выбранных блюд (экземпляров class Dish)
    '''
    if not all([isinstance(member, Dish) for member in dishes_list]):
        return 'Ошибка: не все элементы списка принадлежат class Dish'
    sum_dish = Dish()
    for dish_name in list_of_dishes_names:
        sum_dish += returned_dish(dishes_list, dish_name)
    return sum_dish.shop_dict(count_persons)

# Проба работы с форматами json и csv
def make_json_cook_book(cook_book: dict):
    with open('files\cook_book.json', 'w', encoding='utf-8') as json_f:
        json.dump(cook_book, json_f, ensure_ascii=False, indent=4)

def make_csv_cook_book(dishes_list):
    csv_list = []
    csv_list.append(['Поваренная книга'])
    csv_list.append(['Блюдо', 'Инградиенты', 'Количество', 'Ед.изм.'])
    for dish in dishes_list:
        csv_list.append([dish.name])
        for ingradient, amount in dish.ingradients.items():
            amount_excel = str(amount['quantity']).replace('.', ',')
            csv_list.append(['', ingradient, amount_excel, amount['measure']])
    csv.register_dialect("cb_csv", delimiter=";", quoting=csv.QUOTE_NONE, escapechar="\\", lineterminator='\n')
    with open('files\cook_book.csv', 'w', encoding='cp1251') as csv_f:
        writer = csv.writer(csv_f, 'cb_csv')
        writer.writerows(csv_list)

file_path = 'files\cook_book.txt'
dishes_list = dishes_list_from_file(file_path)
if dishes_list:
    print("\nЗадача № 1 формирование словаря cook_book из файла:\n")
    print('cook_book =')
    pprint(get_cook_book(dishes_list))
    print("=" * 60)
    list_of_dishes_names =  ['Фахитос', 'Омлет']
    count_persons = 3
    print(f"\nЗадача № 2 формирования списка закупок на количество клиентов - {count_persons} чел.")
    print(f"Выбранные блюда: {str(list_of_dishes_names).strip('[]')}:\n")
    pprint(get_shop_list(dishes_list, list_of_dishes_names, count_persons))
    print("=" * 60)
    print()
    print(dishes_list[2])
make_csv_cook_book(dishes_list)