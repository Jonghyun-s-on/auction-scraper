from datetime import datetime, timedelta
from itertools import product
import copy


def generate_form_list(condition: dict):
    list_paths = extract_list_paths(condition)
    list_values = [get_by_path(condition, path) for path in list_paths]
    form_list = []
    for combo in product(*list_values):
        form = copy.deepcopy(condition)
        for path, value in zip(list_paths, combo):
            set_by_path(form, path, value)
        form_list.append(form)

    return form_list


def is_valid_form(form):
    try:
        fmt = "%Y-%m-%d"
        start_date = datetime.strptime(form["start_date_input"], fmt)
        end_date = datetime.strptime(form["end_date_input"], fmt)

        if is_valid_date(start_date, end_date):
            return True
        return False

    except (KeyError, ValueError):
        return False


def is_valid_date(start, end):
    today = datetime.today()

    # start 는 오늘 이상
    if start.date() < today.date():
        print("[ERROR] Form Date 1")
        return False

    # end_date 는 start_date + 14일 이내
    if end > start + timedelta(days=14):
        print("[ERROR] Form Date 2")
        return False

    return True


def extract_list_paths(d, prefix=()):
    paths = []
    for k, v in d.items():
        if isinstance(v, list):
            paths.append(prefix + (k,))
        elif isinstance(v, dict):
            paths.extend(extract_list_paths(v, prefix + (k,)))
    return paths


def get_by_path(data, path):
    for key in path:
        data = data[key]
    return data


def set_by_path(data, path, value):
    for key in path[:-1]:
        data = data.setdefault(key, {})
    data[path[-1]] = value
