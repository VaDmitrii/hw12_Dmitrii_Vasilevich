import logging

from flask import Blueprint, request, render_template

from hw12_Dmitrii_Vasilevich.lesson12_project_source_v3.functions import save_data

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
uploaded_blueprint = Blueprint('uploaded_blueprint', __name__, template_folder='templates')

UPLOAD_FOLDER = "./uploads/images"
ALLOWED_EXTENSIONS = {'jpeg', 'png', 'jpg'}

logger_info = logging.getLogger("info")
logger_error = logging.getLogger('error')


@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template('post_form.html')


@uploaded_blueprint.route("/uploaded", methods=["GET", "POST"])
def page_post_uploaded():
    try:
        picture = request.files.get("picture")
        content = request.form.get("content")
        picture_name = picture.filename
        extension = picture_name.split('.')[-1]
        if extension in ALLOWED_EXTENSIONS:
            save_data(picture_name=picture_name, content=content)
            picture.save(f"{UPLOAD_FOLDER}/{picture_name}")
            return render_template('post_uploaded.html', content=content, picture_name=picture_name)
        elif not picture:
            raise PermissionError
        else:
            logger_info.error(f"Попытка загрузки файла формата '.{extension}'")
            return f'<h1>Загруженный файл - не картинка</h1>'
    except PermissionError:
        logger_error.error("ошибка загрузки изображения")
        return "<h1>ошибка загрузки изображения</h1>"
