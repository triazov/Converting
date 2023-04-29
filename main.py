from PIL import Image
import time


def main_menu():
    print('Для начала конвертации поместите файл ваш в папку IMG Ishod')
    time.sleep(1)
    print('Если вы перенесли следуйте дальше инструкции!')
    time.sleep(1)
    print('Выберите! 1- png to jpg, 2- jpg to png')
    vibor = input()
    if vibor == '1':
        convert_for_png_jpg()
    elif vibor == '2':
        convert_for_jpg_png()
    else:
        print('Вы указали неверную цифру')
    
def convert_for_jpg_png():
    print('Введите название файла (без .jpg, при ошибке в названии скрипт вылетет!)')
    name = input()
    print('Сохранение пошло')
    im = Image.open(f'IMG Ishod\{name}.jpg')
    im.save(f'IMG Result\{name}.png')
    print('Файл сохранен')
    print('Вы перемещены в главное меню')

def convert_for_png_jpg():
    print('Введите название файла (без .png), при ошибке в названии скрипт вылетет!')
    name = input()
    print('Сохранение пошло')
    im = Image.open(f'IMG Ishod\{name}.png')
    im.save(f'IMG Result\{name}.jpg')
    print('Файл сохранен')
    print('Вы перемещены в главное меню')
main_menu()
