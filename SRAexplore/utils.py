def inverse_mapping(f):
    return f.__class__(map(reversed, f.items()))


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


def human_readable_size(size, decimal_places=2):
    for unit in ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]:
        if size < 1024.0 or unit == "PiB":
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def none_string(string):
    if string == "None" or string == "" or string is None:
        return None
    else:
        return string


def convert_date(date1, date2):

    return f"{date1.strftime('%d-%m-%Y')}:{date2.strftime('%d-%m-%Y')}"
