import sys, os

from assistent_project import Assistant

import func

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy import Config
from kivy.properties import ObjectProperty
from kivy.core.window import Window


class MainWidget(FloatLayout):
    text_label = ObjectProperty()
    btn_start = ObjectProperty()
    btn_reminder = ObjectProperty()
    btn_contacts = ObjectProperty()
    btn_recipes = ObjectProperty()
    btn_instruction = ObjectProperty()
    btn_bookmarks = ObjectProperty()
    btn_finish = ObjectProperty()
    scroll = ObjectProperty()
    win_size = 100

    def hide_all(self):
        pass

    def on_press_button_start(self):
        filename = 'instruction2.txt'
        self.hide_all()
        self.text_label.text = func.text_wrap(filename, window_size=self.win_size)
        Assistant().start()

    def on_press_button_finish(self):
        sys.exit(0)

    def on_press_button_reminder(self):
        filename = 'reminder_list.txt'
        self.hide_all()
        self.text_label.text = func.text_wrap(filename, window_size=self.win_size)

    def on_press_button_contacts(self):
        filename = 'numbers_list.txt'
        self.hide_all()
        self.text_label.text = func.text_wrap(filename, window_size=self.win_size)

    def on_press_button_recipes(self):
        filename = 'recipes_list.txt'
        self.hide_all()
        self.text_label.text = func.text_wrap(filename, window_size=self.win_size)

    def on_press_button_instruction(self):
        filename = 'instruction.txt'
        self.hide_all()
        self.text_label.text = func.text_wrap(filename, window_size=self.win_size)

    def on_press_button_googlemarks(self):
        filename = 'bookmarks.txt'
        self.hide_all()
        self.text_label.text = func.text_wrap(filename, window_size=self.win_size)


class MainApp(App):
    def build(self):
        return MainWidget()

def control_files():  # функция проверки наличия файлов
    file_path = ['reminder_list.txt', 'numbers_list.txt', 'recipes_list.txt', 'instruction.txt', 'bookmarks.txt']
    for file in file_path:
        if not (os.path.exists(file)):
            f = open(file, 'w+', encoding='utf-8')
            if file == 'instruction.txt':
                f.write('''Данный голосовой помощник предназначен для упрощения освоения старшим поколением новых технологий.
Голосового помощника зовут Морган.

Чтобы воспользоваться голосовым помощником, нажмите кнопку "Старт".
Чтобы посмотреть заметки, нажмите кнопку "Заметки".
Чтобы посмотреть записную книжку, нажмите кнопку "Телефонная книжка".
Чтобы посмотреть рецепты, нажмите кнопку "Рецепты".
Чтобы посмотреть ваши закладки в браузере "Google", нажмите кнопку "Google закладки".

Функции Морган и команды, по которым они вызываются.

Поздороваться: 'привет', 'добрый день', 'здравствуй'

Попрощаться: 'пока', 'вырубись'

Узнать время: 'текущее время', 'сейчас времени', 'который час'

Выключить компьютер: 'выключи компьютер', 'выруби компьютер'

Узнать погоду: 'какая погода', 'погода', 'погода на улице', 'какая погода на улице'

Добавить контакт в телефонную книжку: 'запиши контакт', 'запиши номер телефона'

Узнать номер телефона по имени: 'номер телефона', 'список контактов', 'контакты'

Удалить контакт из телефонной книжки: 'удалить контакт', 'удали контакт'

Сделать напоминание: 'запомни', 'запомни и напомни попозже', 'сделай заметку'

Узнать заметки на сегодня: 'заметки', 'что на сегодня заплонированно', 'какие сегодня дела',
'есть какие-нибудь заметки на сегодня?', 'заметки на сегодня', 'сегодняшние заметки'

Удалить напоминание: 'удалить заметку', 'удали заметку'

Добавить новый рецепт в книгу рецептов: 'добавить рецепт', 'новый рецепт', 'книга рецептов', 'добавить новый рецепт'

Удалить рецепт: 'удалить рецепт'

Узнать рецепт по названию: 'напомни рецепт', 'напомни рецепт блюда', 'книга рецептов'

Включить калькулятор: 'посчитай', 'включи калькулятор', 'запусти калькулятор', 'калькулятор'

Посмотреть "Google" закладки: 'гугл закладки', 'google закладки', 'закладки' 

Найти что-то в интернете: скажите "найди" и то, что хотите найти ''')
            f.close()

if __name__ == '__main__':
    Config.set("graphics", "resizable", 1)
    Config.set("graphics", "width", 1024)
    Config.set("graphics", "height", 1200)
    control_files()
    Assistant().parse_bookmarks()
    app = MainApp()
    app.run()
