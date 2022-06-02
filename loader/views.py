from flask import render_template, Blueprint, request
from functions import new_post_to_json
import logging
from config import ALLOWED_EXTENSIONS
from config import UPLOAD_FOLDER


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/post/", methods=["POST"])
def page_loader_post():
    """Добавление поста"""
    content = request.form.get("content")
    picture = request.files.get("picture")  # Получаем объект картинки из формы
    if not content or not picture:
        return 'Получены не все данные'
    filename = picture.filename  # Получаем имя файла у загруженного файла
    extension = filename.split(".")[-1]  # расширение файла
    # new_picture = f'{UPLOAD_FOLDER}/{filename}'
    new_picture = f'{filename}'

    if extension in ALLOWED_EXTENSIONS:

        picture.save(new_picture)
        new_post_to_json(new_picture, content)

        return render_template('post_uploaded.html', picture=new_picture, content=content)
    else:
        logging.info('Пост не загружен, картинка не соответствует доступным расширениям')
        return 'Пост не загружен, картинка не соответствует доступным расширениям'


@loader_blueprint.route("/post/", methods=["GET", "POST"])
def page_loader_new_post():
    """Страница добавления поста"""
    return render_template('post_form.html')
