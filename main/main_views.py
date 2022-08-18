import logging

from flask import Blueprint, render_template, request

from hw12_Dmitrii_Vasilevich.lesson12_project_source_v3.functions import search_post

index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')
search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')

logger_info = logging.getLogger("info")


@index_blueprint.route('/')
def page_index():
    return render_template('index.html')


@search_blueprint.route('/search')
def page_tag():
    tag = request.args.get('s')
    posts = search_post(tag)
    try:
        if len(posts) > 0:
            logger_info.info(f'запрошен пост по тегу {tag}')
            return render_template('post_list.html', posts=posts, tag=tag)
        else:
            logger_info.error(f"нет указанного ключа '{tag}' в поле 'content'")
            raise KeyError
    except KeyError:
        return "<h1>Tag not found. Try another tag</h1>"
