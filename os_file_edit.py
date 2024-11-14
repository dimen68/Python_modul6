# Файлы в операционной системе
import os, time

directory = '.'
n = 0
dir_size = 0
for directory, dirs, files in os.walk(directory):
    for file in files:
        n += 1
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(f'{directory}\\{file}')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(f'{directory}\\{file}')
        dir_size += filesize
        parent_dir = os.path.dirname(f'{directory}\\{file}')
        print(
            f'Обнаружен файл №{n}: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, \n  Родительская директория: {parent_dir}')
print(f'\nОбщий размер папки: {round(dir_size / 1024, 2)} Кбайт')
