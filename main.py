

def get_unique_id(id_dict):
    orig_id = []
    for count, user in enumerate(id_dict):
        y = list(id_dict.values())[count]
        orig_id = orig_id + y
    x = set(orig_id)
    return x


def request_percent(data_list):
    y = []

    for count, i in enumerate(data_list):
        y.append(len(data_list[count].split()))

    values_set = set(y)
    result_dict = {}
    for number in values_set:
        percent = f'{round(y.count(number) * 100 / len(data_list))} процентов'
        result_dict[f'Запросов с {number} словами'] = percent

    return result_dict


def get_max_value(data_dict):
    value_list = []

    for name, value in data_dict.items():
        value_list.append(value)

    for count, big in enumerate(value_list):
        if big == max(value_list):
            return list(data_dict.keys())[count]

