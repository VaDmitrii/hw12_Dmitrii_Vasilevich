import logging

from flask import Flask, send_from_directory

from main.main_views import index_blueprint, search_blueprint

from loader.loader_views import loader_blueprint, uploaded_blueprint


app = Flask(__name__)

logger_info = logging.getLogger("info")
logger_error = logging.getLogger('error')

info_handler = logging.FileHandler("info.txt")
error_handler = logging.FileHandler("error.txt")

logger_info.addHandler(info_handler)
logger_error.addHandler(error_handler)

formatter = logging.Formatter("%(asctime)s : %(message)s : %(funcName)s")
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

app.register_blueprint(index_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(loader_blueprint)
app.register_blueprint(uploaded_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
