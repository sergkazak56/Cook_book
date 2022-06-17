from pprint import pprint
import sys

class Dish():

    def __init__(self, dish_name):
        self.name = dish_name
        self.ingradients = []

    def add_ingradient(self, name, quantity, measure):
        ingradient = {}
        ingradient['ingredient_name'] = name
        ingradient['quantity'] = quantity
        ingradient['measure'] = measure
        self.ingradients.append(ingradient)


def cook_book_from_file(file_path):
    cook_book = {}
    with open(file_path, encoding='utf-8-sig') as f_cook_book:
        for line in f_cook_book:
            if not line.strip():
                return
            new_dish = Dish(line.strip())
            quantity_ingradients = int(f_cook_book.readline().strip())
            for item in range(quantity_ingradients):
                ingradient_list = f_cook_book.readline().strip().split(' | ')
                new_dish.add_ingradient(ingradient_list[0], ingradient_list[1], ingradient_list[2])
            cook_book[new_dish.name] = new_dish.ingradients
            f_cook_book.readline()
    return cook_book

file_path = 'files\cook_book.txt'
pprint(cook_book_from_file(file_path))