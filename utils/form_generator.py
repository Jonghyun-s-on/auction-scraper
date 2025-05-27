from itertools import product
import copy

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