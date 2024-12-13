import sqlite3
from config import DB_PATH


def add_post(title: str, content: str) -> None:
    add_post_query = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(add_post_query, (title, content))
    connection.commit()
    connection.close()

    print("Пост добавлен")


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


def delete_post(post_id: int) -> None:
    delete_post_query = """
    DELETE FROM posts WHERE post_id = ?
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(delete_post_query, (post_id,))
    connection.commit()
    connection.close()

    return f"Удалено постов: {cursor.rowcount}"


def get_post(post_id: int) -> None:
    get_post_query = """

    """

    # Сделать проверку существует ли пост и менять ответ программы
    print(f"Вот пост с id: {post_id}.", post)


def update_post(post_id: int, new_title: str, new_content: str) -> None:
    update_post_query = """
    UPDATE posts SET title = ?, content = ? WHERE post_id = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        update_post_query,
        (new_title, new_content, post_id),
    )

    updated_rows_count = cursor.rowcount

    connection.commit()
    connection.close()

    if updated_rows_count == 0:
        print("Пост для обновления не найден")
    else:
        print("Пост обновлен")
