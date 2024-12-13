from flask import Flask

app = Flask(__name__)

weather = {
    "astana": -10.3,
    "almaty": -6.7,
    "vienna": 0.0,
}
todos = []


@app.route("/")
def welcome():
    return "Это моё первое API"


@app.route("/name")
def get_name():
    return "Аяулым"


@app.route("/todos/new/<title>")
def add_task(title):
    todos.append(title)
    return f"Задача '{title}' добавлена!"


@app.route("/todos")
def get_tasks():
    if todos:
        return f"Список задач: {', '.join(todos)}"
    return "Список задач пуст"


@app.route("/todos/remove/<index>")
def remove_task(index):
    if index.isdigit() and 0 <= int(index) < len(todos):
        task = todos.pop(int(index))
        return f"Задача '{task}' с индексом {index} удалена!"
    return "Задание не найдено"


@app.route("/todos/get/<index>")
def get_task(index):
    if index.isdigit() and 0 <= int(index) < len(todos):
        return f"Задача с индексом {index}: {todos[int(index)]}"
    return "Задание не найдено"


@app.route("/todos/edit/<index>/<new_title>")
def edit_task(index, new_title):
    if index.isdigit() and 0 <= int(index) < len(todos):
        todos[int(index)] = new_title
        return f"Задача с индексом {index} изменена на '{new_title}'"
    return "Задание не найдено"


@app.route("/city/<city_name>")
def get_city_weather(city_name):
    city_name = city_name.lower()
    if city_name in weather:
        temp = weather[city_name]
        return f"Текущая погода в {city_name.capitalize()}: {temp}°C"
    return f"Нет информации о погоде в {city_name}"


if __name__ == "__main__":
    app.run(port=5007, host="0.0.0.0", debug=True)
