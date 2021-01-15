from tkinter import *
from filmBase import *
from Blocks import *

# Функция очищает элементы интерфейса
def clear():
	open_block.hide()
	save_block.hide()
	add_block.hide()
	delete_block.hide()

# Функции для отображения интерфейса
def open_list():
	clear()
	open_block.show()

def save_list():
	clear()
	save_block.show()

def add_film():
	clear()
	add_block.show()

def delete_film():
	clear()
	delete_block.show()

def exit():
    pass


# Создаем основное окно и задаем размеры
root = Tk()
root.geometry('1000x800+500+100')

# Создаем и задаем размеры фреймам для меню и контента
menu = Frame(root, width=180, height=800, bg='gray')
screen = Frame(root, width=820, height=600, bg='#4f5582')
editor = Frame(root, width=820, height=200, bg='#4169E1')
menu.place(x=0, y=0)
screen.place(x=180, y=0)
editor.place(x=180, y=600)

#Создаем кнопки меню
open_list_btn = Button(menu, text='Открыть список', command=open_list)
save_list_btn = Button(menu, text='Сохранить список', command=save_list)
add_film_btn = Button(menu, text='Добавить фильм', command=add_film)
delete_film_btn = Button(menu, text='Удалить фильм', command=delete_film)
exit_btn = Button(menu, text='Выход', command=exit)

#Размещаем кнопки меню
open_list_btn.place(x=0, y=30, width=180, height=40)
save_list_btn.place(x=0, y=70, width=180, height=40)
add_film_btn.place(x=0, y=110, width=180, height=40)
delete_film_btn.place(x=0, y=150, width=180, height=40)
exit_btn.place(x=0, y=190, width=180, height=40)

# Создаем и разъмещаем canvas на котором будет отрисовываться таблица
canvas = scrolledtext.ScrolledText(screen, width=95, height=35)
canvas.place(x=20,y=10)

# Создаем базу фильмов
base = FilmsBase()

# Создаем блоки интерфейса
open_block = OpenMenu(editor, base, canvas)
save_block = SaveMenu(editor, base, canvas)
add_block = AddMenu(editor, base, canvas)
delete_block = DeleteMenu(editor, base, canvas)

root.mainloop()
