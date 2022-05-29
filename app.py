from flask import Flask, send_from_directory

import logging
from loader.views import loader_blueprint
from main.views import main_blueprint

# logging.basicConfig(level=logging.INFO, filename="basic.log", encoding='utf8')  # filename - логирование исключений в файл
# logging.basicConfig(level=logging.ERROR, filename="error.log", encoding='utf8')

app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)  # url_prefix='/'

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route("/uploads/<path:path>", methods=["GET", "POST"])
def static_dir(path):
    return send_from_directory("./uploads/images", path)


if __name__ == '__main__':
    app.run(debug=True)
