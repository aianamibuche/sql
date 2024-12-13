# pip install Flask - установка Flask. пишем в терминале

from flask import Flask

from sql_practice import add_post, delete_post, update_post, get_posts


# создание объекта Flask - создали приложение
app = Flask(__name__)

# Global variables
weather = {
    "astana": -10.3,
    "almaty": -6.7,
    "vienna": 0,
}
todos = []


# 127.0.0.1:5000/
@app.route("/")
def welcome():
    return "Это моё первое API"


# Создать обработчик, чтобы при запросе на /name, возвращалось ваше Имя
@app.route("/name")
def get_name():
    return "Арман"


# http://10.60.3.31:5000/city/Astana
@app.route("/city/<city_name>")
def weather_by_city(city_name):
    return city_name


# 1. Добавления поста
@app.route("/posts/add/<post_title>/<post_content>")
def add_new_post(post_title, post_content):
    return []


# 2. Получение всех постов
@app.route("/posts")
def get_all_posts():
    return get_posts()


# 3. Удаление поста по post_id
@app.route("/posts/delete/<post_id>")
def delete_post_by_id(post_id):
    return delete_post(post_id)


# 4. Обновление поста по post_id
@app.route("/posts/update/<post_id>/<new_title>/<new_content>")
def update_post_by_id(post_id, new_title, new_content):
    return []


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
