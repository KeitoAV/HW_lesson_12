import logging
from flask import render_template, Blueprint, request
from functions import get_content

# создаем блюпринт, выбираем для него имя, добавляем настройку папки с шаблонами
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def page_main_index():
    """Главная страница"""
    logging.info('Главная страница запрошена')
    return render_template('index.html')


@main_blueprint.route('/search/')
def page_main_post():
    """Страница поиска"""

    s = request.args.get('s', '')
    logging.info(f'Страница {s} запрошена')

    content_list = get_content(s)
    # return content_list
    if content_list == "Пост не найден":
        logging.info(f'Не найдено постов по введённому запросу')
        return 'Не найдено постов по введённому запросу'
    else:
        return render_template("post_list.html", s=s, content_list=content_list)


