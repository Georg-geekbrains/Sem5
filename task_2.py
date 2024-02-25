"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os
file_path = '/home/user/documents/file.txt'
def split_file_path(file_path):
    path, file_name = os.path.split(file_path)
    file_base, file_ext = os.path.splitext(file_name)
    return path, file_base, file_ext
print(split_file_path(file_path))