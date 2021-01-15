import tkinter as tk 

class FilmsBase(object):
    """Класс для реализации функционала базы фильмов"""

    def __init__(self):
        self.file_extension = '.flm'
        self.file_base = None
        self.saved = False
        self.base = []
        self.colms_title = ['№_', 'Название', 'Оценка', 'Режиссер',]
        self.colms_len = []
        self.meta_data = [0, 4,
                          len(self.colms_title[1]),
                          len(self.colms_title[2]),
                          len(self.colms_title[3]),]
        

    def write_metadata(self):
        """Вспомогательная функция, которая записывает метаданные в файл"""
        self.file_base.write('{}#{}#{}#{}#{}\n'.format(str(self.meta_data[0]),
                                                     str(self.meta_data[1]),
                                                     str(self.meta_data[2]),
                                                     str(self.meta_data[3]),
                                                     str(self.meta_data[4])))

    def edit_metadata(self):
        """
        Функция для изменения метаданных.
        Обходит всю базу данных, считает колличество фильмов,
        максимальную длину столбца и записывает эти данные.
        """
        nums = 0
        max_len_name = len(self.colms_title[1])
        max_len_rat = len(self.colms_title[2])
        max_len_prod = len(self.colms_title[3])
        for film in self.base:
            if len(film[0]) > max_len_name:
                max_len_name = len(film[0])
            if len(film[1]) > max_len_rat:
                max_len_rat = len(film[1])
            if len(film[2]) > max_len_prod:
                max_len_prod = len(film[2])
            nums += 1
        self.meta_data = [nums, 4, 
                          max_len_name, 
                          max_len_rat, 
                          max_len_prod]


    def save_base(self, base_name):
        """
        Функция для сохранения базы фильмов.
        Создает или перезаписывает файл, построчно записывает в него
        данные фильмов в специальном формате
        """
        self.saved = True
        base_name += self.file_extension
        self.file_base = open(base_name, 'w')
        self.write_metadata()
        for film in self.base:
            self.file_base.write('{}/{}/{}\n'.format(film[0],
                                                      film[1], 
                                                      film[2]))
        self.file_base.close()

    def load_base(self, base_name):
        """Функция загружает базу из файла"""
        self.saved = True
        self.base.clear()
        base_name += self.file_extension
        self.file_base = open(base_name, 'r')

        # Считываем метаданные из файла и записываем их
        for data in self.file_base:
            split_data = data.split('#')
            break
        self.meta_data.clear()
        for data in split_data:
            self.meta_data.append(int(data))
        self.edit_metadata()

        # Считываем из файла строки фильмов
        for film in self.file_base:
            data = film.split('/')
            data[2] = data[2][:-1]
            self.base.append(data)

        self.file_base.close()

    def add_film(self, name, rat, director):
        """
        Добавляет фильм.
        Если база пустая, просто добавляет фильм.
        Если рейтинг фильма ниже, чем рейтинг последнего фильма в списке,
        добавляет филм в конец.
        Иначе, ищет первый фильм, рейтинг которого будет меньше и вставляет
        перед ним.
        """
        self.saved = False
        index = 0
        if len(self.base) == 0:
            self.base.append([name, rat, director])
        elif float(rat) < float(self.base[-1][1]):
            self.base.append([name, rat, director])
        else:
            for film in self.base:
                if float(rat) >= float(film[1]):
                    self.base.insert(index, [name, rat, director])
                    break
                else:
                    index += 1
        self.edit_metadata()


    def delete_film(self, name):
        """Ищет в базе фильм с заданным именем и удаляет его"""
        self.saved = False
        index = 0
        for film in self.base:
            if name == film[0]:
                self.base.remove(film)
                break
            else:
                index += 1
        self.edit_metadata()

    

    def make_colm(self, n_col, el):
        """Исходя  из максимальной дляны колонки, выравнивает текст по центру"""
        indent = self.meta_data[n_col] - len(el)
        if indent % 2 == 0:
            indent = indent // 2
            out = (' ' * indent) + el + (' ' * indent)
            return out
        else:
            indent = indent // 2
            out = (' ' * indent) + el + (' ' * (indent + 1))
            return out


    def print_base(self, canvas):
        """Печатает базу"""
        canvas.delete(1.0, tk.END)
        index = 1
        for film in self.base:
            row = ('|' + self.make_colm(1, str(index)) + '|' +
                   self.make_colm(2, film[0]) + '|' +
                   self.make_colm(3, film[1]) + '|' + 
                   self.make_colm(4, film[2]) + '|\n')
            canvas.insert(tk.INSERT, row)
            index += 1







        

        