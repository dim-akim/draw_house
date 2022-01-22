"""
1 шаг. Запуск простейшего сервера на Flask

Этапы:

Импорт основного класса.

Создание экземпляра класса.

Декоратор, в котором описан путь. По этому URL будет обращаться пользователь.

Функция, которая вызывается при обращении пользователя к пути, указанному в декораторе.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():    # Функция просмотра
    return 'Hello, World!'    # вернуть текст!


if __name__ == '__main__':
    app.run()