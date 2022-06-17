from pprint import pprint
import sys



def cook_book_from_file(file_path):
    cook_book = {}
    with open(file_path, encoding='utf-8-sig') as f_cook_book:
        for line in f_cook_book:
            if not line.strip():
                return
            dish_name = line.strip()
            quantity_ingradients = int(f_cook_book.readline().strip())
            ingradients = []
            for item in range(quantity_ingradients):
                ingradient_dict = {}
                ingradient_list = f_cook_book.readline().strip().split(' | ')
                ingradient_dict['ingredient_name'] = ingradient_list[0]
                ingradient_dict['quantity'] = int(ingradient_list[1])
                ingradient_dict['measure'] = ingradient_list[2]
                ingradients.append(ingradient_dict)
            cook_book[dish_name] = ingradients
            f_cook_book.readline()
    return cook_book

file_path = 'files\cook_book.txt'
pprint(cook_book_from_file(file_path))
