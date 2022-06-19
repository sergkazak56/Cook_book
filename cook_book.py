from pprint import pprint

# Процедурный метод

def get_cook_book_from_file(file_path):
    '''
    :param: file_path - путь к файлу с данными по блюдам
    :return: cook-book - словарь из блюд и их инградиентов
    Функция формирует словать cook-book из текстового файла с разделителями
    '''
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
                ingradient_dict['quantity'] = float(ingradient_list[1])
                ingradient_dict['measure'] = ingradient_list[2]
                ingradients.append(ingradient_dict)
            cook_book[dish_name] = ingradients
            f_cook_book.readline()
    return cook_book

def get_shop_list(cook_book, dishes, person_count = 1, file_path = 'files\shop_list.txt'):
    '''
    :param cook_book - словарь из блюд и их инградиентов
    :param dishes - список блюд, для которых надо составить список покупки
    :param person_count -  количество персон, для которых рассчитываются блюда (по умолчанию = 1)
    :return: shop_dict - словарь список инградиентов с необходимым количеством для закупки
    Функция выводит список необходимых покупок в словарь cook_book и в файл files\shop_list.txt
    для удобства распечатывания
    '''
    shop_dict = {}
    if not dishes or not cook_book:
        return
    for dish in dishes:
        ingradients = cook_book[dish]
        for ingradient in ingradients:
            if ingradient['ingredient_name'] in shop_dict:
                shop_dict[ingradient['ingredient_name']]['quantity'] += ingradient['quantity'] * person_count
            else:
                amount_ingradient = {}
                amount_ingradient['measure'] = ingradient['measure']
                amount_ingradient['quantity'] = ingradient['quantity'] * person_count
                shop_dict[ingradient['ingredient_name']] = amount_ingradient
    with open(file_path, 'w', encoding='utf-8') as f_shop_list:
        f_shop_list.write(f'\tСПИСОК ИНГРЕДИЕНТОВ для закупки:\n\t{"-" * 33}\n')
    with open(file_path, 'a', encoding='utf-8') as f_shop_list:
        for ingradient, amount in shop_dict.items():
            str_to_file =f"\t{ingradient} - {amount['quantity']} {amount['measure']}\n"
            f_shop_list.write(str_to_file)
    return shop_dict

file_path = 'files\cook_book.txt'
print("Задача № 1 формирования словаря cook_book из файла:\n")
print('cook_book =')
cook_book = get_cook_book_from_file(file_path)
pprint(cook_book)
print("=" * 60)
list_of_dishes_names =  ['Фахитос', 'Омлет']
count_persons = 3
print(f"\nЗадача № 2 формирования списка закупок на количество клиентов - {count_persons} чел.")
print(f"Выбранные блюда: {str(list_of_dishes_names).strip('[]')}:\n")
pprint(get_shop_list(cook_book, list_of_dishes_names, count_persons))
print("=" * 60)