import os

# Функция сортировки файлов по количеству строк и их обЪединения
def merging_files(path, merging_file_name = 'merging_file.txt'):
    '''
    :param path - путь к директории где находятся входные файлы
    :param merging_file_name - название объединяющего файла
    :return: возвращает строку успешного завершения или ошибки
    Функция сортирует входные файлы по количеству строк в них и выводит в
    объединяющий файл по возрастанию количества строк - название входного файла,
    количество строк, содержание файла. Объединяющий файл создается в
    текущем каталоге.
    '''
    if not os.path.exists(path):
        return 'Ошибка: задан не существующий путь к файлам'
    if not merging_file_name:
        return 'Ошибка: не задано имя файла для вывода результата'
    file_names = os.listdir(path)
    if not file_names:
        return 'Ошибка: каталог входных файлов пуст'
    file_path_in = os.path.join(os.getcwd(), merging_file_name)
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
    return f'Файлы успешно объединены в файле: {merging_file_name}, находящемся в текущем каталоге.'

CATALOG_NAME = 'files_for_merge'
BASE_PATH = os.getcwd()
path = os.path.join(BASE_PATH, CATALOG_NAME)
print(merging_files(path, 'merging_file.txt'))
