#  Записать и запомнить
strings_positions = {}

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    line_nmb = 1
    for string in strings:
        pos_ = file.tell()
        file.write(string +'\n')
        strings_positions[(line_nmb, pos_)] = string
        line_nmb += 1
    file.close()
    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)