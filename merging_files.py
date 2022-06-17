import os

def merging_files(path, file_names, merging_file_name):
    '''
    :param path - путь к директории где находятся входные и выходной файлы
    :param file_names - список имен файлов, которые надо объединить
    :param merging_file_name - название объединяющего файла
    :return: возвращает строку успешного завершения или ошибки
    Функция сортирует входные файлы по количеству строк в них и выводит в
    объединяющий файл по возрастанию количества строк - название входного файла,
    количество строк, содержание файла.
    '''
    if not path or not file_names or not merging_file_name:
        return 'Ошибка: один из параметров функции add_file_to_new_one пустой'
    file_path_in = os.path.join(path, merging_file_name)
    files_dict = {}
    for file_name in file_names:
        file_path_out = os.path.join(path, file_name)
        with open(file_path_out, encoding='utf-8-sig') as read_f:
            files_dict[len(read_f.readlines())] = file_name
    files_dict_sorted = dict(sorted(files_dict.items()))
    with open(file_path_in, 'w', encoding='utf-8') as merging_f:
        for len_file, file_name in files_dict_sorted.items():
            file_path_out = os.path.join(path, file_name)
            with open(file_path_out, encoding='utf-8-sig') as read_f:
                merging_f.write(f"{file_name}\n")
                merging_f.write(f"{len_file}\n")
                merging_f.write(read_f.read())
                merging_f.write('\n')
    return f'Файлы успешно обединены в файле: {merging_file_name}, находящемся в каталоге: {path}'

CATALOG_NAME = 'files_for_merge'
BASE_PATH = os.getcwd()
files_names = ['1.txt', '2.txt', '3.txt']
path = os.path.join(BASE_PATH, CATALOG_NAME)
print(merging_files(path, files_names, 'merging_file'))
