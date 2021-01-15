from filmBase import *
from tkinter import *
from tkinter import scrolledtext 
from tkinter import messagebox
import os.path
import tkinter as tk 


class OpenMenu(object):
    """Класс для меню открытия базы фильмов"""

    def __init__(self, main_frame, base_obj, canvas):
        """Инициализация элементов меню"""
        self.canvas = canvas
        self.base_obj = base_obj
        self.caption = Label(main_frame, text='Введите название базы:')
        self.enter = Entry(main_frame, width=30)
        self.btn = Button(main_frame, text='Открыть список', command=self.open_list)


    def open_list(self):
        """
        Фунцкция, вызываемая при нажатии на кнопку "Открыть".
        Находит файл с введенным именем, считывает изнего данные
        и записывает их в базу. Если пользователь перед этим работал с
        другой базой, то появится предупреждение.
        """
        name = self.enter.get()
        self.enter.delete(0, tk.END)
        if os.path.exists(name + self.base_obj.file_extension) == False:
            messagebox.showwarning('Ошибка', '!!Списка с таким именем не существует!!')
        elif len(self.base_obj.base) != 0 and self.base_obj.saved != True:
            res = messagebox.askyesno('Предупреждение',
                                    """Вы пытаетесь открыть новый список,\
                                    все не сохраненные данные будут потеряны. Вы уверны?""")
            if res == True:
                self.base_obj.load_base(name)
                self.base_obj.print_base(self.canvas)
        else:
            self.base_obj.load_base(name)
            self.base_obj.print_base(self.canvas)


    def show(self):
        """Выводит элементы данного меню на экран"""
        self.caption.place(x=30,y=20)
        self.enter.place(x=30, y=50)
        self.btn.place(x=230, y=50)

    def hide(self):
        """Убирает элементы меню с экрана"""
        self.caption.place_forget()
        self.enter.place_forget()
        self.btn.place_forget()


class SaveMenu(object):
    """Класс для меню сохранения базы фильмов"""

    def __init__(self, main_frame, base_obj, canvas):
        """Инициализация элементов меню"""
        self.canvas = canvas
        self.base_obj = base_obj
        self.caption = Label(main_frame, text='Введите название базы:')
        self.enter = Entry(main_frame, width=30)
        self.btn = Button(main_frame, text='Сохранить список', command=self.save_list)

    def save_list(self):
        """Функция сохраняет базу в файл, с введеным именем"""
        name = self.enter.get()
        self.enter.delete(0, tk.END)
        self.base_obj.save_base(name)

    def show(self):
        """Выводит элементы данного меню на экран"""
        self.caption.place(x=30,y=20)
        self.enter.place(x=30, y=50)
        self.btn.place(x=230, y=50)

    def hide(self):
        """Убирает элементы меню с экрана"""
        self.caption.place_forget()
        self.enter.place_forget()
        self.btn.place_forget()

class AddMenu(object):
    """Класс для меню добавления фильма в базу"""

    def __init__(self, main_frame, base_obj, canvas):
        """Инициализация элементов меню"""
        self.canvas = canvas
        self.base_obj = base_obj
        self.name_caption = Label(main_frame, text='Название фильма:')
        self.rating_caption = Label(main_frame, text='Рейтинг фильма:')
        self.producer_caption = Label(main_frame, text='Режиссер:')
        self.name_enter = Entry(main_frame, width=30)
        self.rating_enter = Entry(main_frame, width=30)
        self.producer_enter = Entry(main_frame, width=30)
        self.add_btn = Button(main_frame, text='Добавить фильм', command=self.add_film)

    def add_film(self):
        """Функция собирает данные из полей ввода и добавляет новый фильм в базу"""
        name = self.name_enter.get()
        rating = self.rating_enter.get()
        producer = self.producer_enter.get()
        self.name_enter.delete(0, tk.END)
        self.rating_enter.delete(0, tk.END)
        self.producer_enter.delete(0, tk.END)
        self.base_obj.add_film(name, rating, producer)
        self.base_obj.print_base(self.canvas)

    def show(self):
        """Выводит элементы данного меню на экран"""
        self.name_caption.place(x=10, y=10)
        self.name_enter.place(x=10, y=40)
        self.rating_caption.place(x=10, y=70)
        self.rating_enter.place(x=10, y=100)
        self.producer_caption.place(x=10, y=130)
        self.producer_enter.place(x=10, y=160)
        self.add_btn.place(x=400, y=100)

    def hide(self):
        """Убирает элементы меню с экрана"""
        self.name_caption.place_forget()
        self.name_enter.place_forget()
        self.rating_caption.place_forget()
        self.rating_enter.place_forget()
        self.producer_caption.place_forget()
        self.producer_enter.place_forget()
        self.add_btn.place_forget()

class DeleteMenu(object):
    """Класс для меню удаления фильма из базы"""

    def __init__(self, main_frame, base_obj, canvas):
        """Инициализация элементов меню"""
        self.canvas = canvas
        self.base_obj = base_obj
        self.caption = Label(main_frame, text='Введите название фильма:')
        self.enter = Entry(main_frame, width=30)
        self.btn = Button(main_frame, text='Удалить фильм', command=self.delete_film)

    def delete_film(self):
        """Функция удаляет фильм, с указанным именем, из базы"""
        name = self.enter.get()
        self.enter.delete(0, tk.END)
        self.base_obj.delete_film(name)
        self.base_obj.print_base(self.canvas)

    def show(self):
        """Выводит элементы данного меню на экран"""
        self.caption.place(x=30,y=20)
        self.enter.place(x=30, y=50)
        self.btn.place(x=230, y=50)

    def hide(self):
        """Убирает элементы меню с экрана"""
        self.caption.place_forget()
        self.enter.place_forget()
        self.btn.place_forget()



        
        





