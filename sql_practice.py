import sqlite3
from config import DB_PATH


def add_post(title, content):
    add_post_query = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(add_post_query, (title, content))
    connection.commit()
    connection.close()
    return "Пост добавлен"


def update_post(post_id, new_title, new_content):
    update_post_query = """
    UPDATE posts SET title = ?, content = ? WHERE post_id = ?;
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(update_post_query, (new_title, new_content, post_id))
    connection.commit()
    updated_rows = cursor.rowcount
    connection.close()
    return "Пост обновлен" if updated_rows > 0 else "Пост не найден"


add_post("Заголовок", "Содержание")
update_post(1, "Обновленный заголовок", "Обновленное содержание")
