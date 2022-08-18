import json

import logging

from json import JSONDecodeError

from typing import Any

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

logger_error = logging.getLogger('error')


def load_data(path) -> list[set] | Any:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            posts = json.loads(file.read())
            return posts
    except (JSONDecodeError, FileNotFoundError):
        logger_error.error("Ошибка загрузки файла JSON")
        return "<h2>Файл отсутствует или поврежден</h2>"


def search_post(tag: str) -> str | list[set]:
    post_search = []
    for line in load_data(POST_PATH):
        content = line["content"].replace('!', '')
        if '#' + tag.lower() in content.split(' '):
            post_search.append(line)
    return post_search


def save_data(picture_name, content) -> None:
    item = {'pic': f'/uploads/images/{picture_name}', 'content': content}
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data.append(item)
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
