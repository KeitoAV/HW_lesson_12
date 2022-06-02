import json
import logging
from json import JSONDecodeError
from pprint import pprint as pp

from config import POST_PATH


def load_json(path=POST_PATH):
    """Загрузка данных из файла json, проверка ошибок"""
    try:
        with open(path, 'r', encoding='utf8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        logging.error("Ошибка доступа к файлу")
    except JSONDecodeError:
        logging.error("Файл не удается преобразовать")  # Будет выполнено если файл найден, но не превращается из JSON


# pp(load_json())


def get_content(s):
    """Возвращает content по заданному в поиск слову"""
    posts = load_json()
    content_list = []

    for post in posts:
        if s.lower() in post['content'].lower():
            content_list.append(post)

    if len(content_list) == 0:
        return 'Пост не найден'
    return content_list


# pp(get_content('закат'))


def new_post_to_json(new_picture, new_content):
    """Добавляет новый пост, проверка ошибок"""
    all_posts = load_json(POST_PATH)
    try:
        new_post = {"pic": new_picture, "content": new_content}
        all_posts.append(new_post)
        with open(POST_PATH, 'w', encoding='utf8') as file:
            json.dump(all_posts, file, ensure_ascii=False, indent=2)
            logging.info('Пост добавлен!')

        return all_posts
    except FileNotFoundError:
        logging.error("Ошибка доступа к файлу")
    except JSONDecodeError:
        logging.error("Файл не удается преобразовать")

# pp(new_post_to_json('фото', 'текст'))
