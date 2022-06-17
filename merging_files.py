import os

def add_file_to_new_one(path, file_names, merging_file_name):
    if not path or not file_names or not merging_file_name:
        return 'Ошибка: не указан один из параметров функции'
    file_path_in = os.path.join(path, merging_file_name)
    with open(file_path_in, 'w', encoding='utf-8') as merging_f:
        pass
    for file_name in file_names:
        file_path_out = os.path.join(path, file_name)
        with open(file_path_out, encoding='utf-8-sig') as read_f:
            lines = read_f.readlines()
            with open(file_path_in, 'a', encoding='utf-8') as merging_f:
                merging_f.write(f"{file_name}\n")
                merging_f.write(f"{len(lines)}\n")
                for line in lines:
                    merging_f.write(line)
                merging_f.write('\n')
    return f'Файлы успешно обединены в файле {merging_file_name}, находящемся в каталоге {path}'

CATALOG_NAME = 'files_for_merge'
BASE_PATH = os.getcwd()
files_names = ['1.txt', '2.txt', '3.txt']
path = os.path.join(BASE_PATH, CATALOG_NAME)
print(add_file_to_new_one(path, files_names, 'merging_file'))
