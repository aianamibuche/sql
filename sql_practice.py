import sqlite3
from config import DB_PATH


def add_post(title: str, content: str):
    add_post_query = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(add_post_query, (title, content))
    connection.commit()
    connection.close()
    return "Пост добавлен"


def get_posts():
    get_posts_query = """
    SELECT * FROM posts;
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_posts_query)
    posts = cursor.fetchall()
    connection.close()
    return posts


def delete_post(post_id: int):
    delete_post_query = """
    DELETE FROM posts WHERE post_id = ?;
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(delete_post_query, (post_id,))
    connection.commit()
    deleted_rows = cursor.rowcount
    connection.close()
    return f"Удалено постов: {deleted_rows}"


def get_post(post_id: int):
    get_post_query = """
    SELECT * FROM posts WHERE post_id = ?;
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_post_query, (post_id,))
    post = cursor.fetchone()
    connection.close()
    return post


def update_post(post_id: int, new_title: str, new_content: str):
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
print(get_posts())
print(get_post(2))
update_post(1, "Обновленный заголовок", "Обновленное содержание")
print(get_post(1))
delete_post(1)
print(get_posts())
