
def custom_write(file_name, strings):  # file_name - название файла для записи, strings - список строк для записи.
    file = open(file_name, 'w',encoding='utf-8')
    strings_positions = {}
    str_num = 0
    str_start_byte = file.seek(0)  # байт начала первой строки
    for string_ in strings:
        file.write(string_ + '\n')
        str_num += 1
        key = (str_num, str_start_byte)  # задаём ключи словаря
        strings_positions[key] = string_  # добавляем значения в словарь
        str_start_byte = file.tell()
    file.close()
    return strings_positions

file_name = 'test.txt'
info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)