from datetime import datetime, timedelta
from itertools import product
from src.utils.logger import logger
import copy


def generate_valid_forms(condition: dict):
    return [form for form in generate_form_list(condition) if is_valid_form(form)]


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


def is_valid_form(form: dict):
    return is_valid_date_range(form)


def is_valid_date_range(form: dict):
    try:
        fmt = "%Y-%m-%d"
        start = datetime.strptime(form["start_date_input"], fmt)
        end = datetime.strptime(form["end_date_input"], fmt)

        today = datetime.today()

        if start.date() < today.date():
            logger.warning(f"START_DATE is earlier than today. (input value: {start.date()}, today: {today.date()})")
            raise ValueError("invalid START_DATE")

        if end > start + timedelta(days=14):
            logger.warning(f"END_DATE exceeds 14 days after START_DATE. (input value: {start.date()} ~ {end.date()})")
            raise ValueError("invalid END_DATE")

        return True

    except KeyError as e:
        logger.warning(f"missing date field in form: {e}")
        return False


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
