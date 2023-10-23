import csv


def get_list() -> list:
    with open('number_plate.csv', 'r') as csv_f:
        result_list = []
        reader = csv.DictReader(csv_f)
        for row in reader:
            result_list.append(row)
        return result_list


def search_prefecture(data_list: list, prefecture_name: str) -> list:
    return list(filter(lambda x: prefecture_name in x['prefecture'], data_list))


def search_plate_name(data_list: list, plate_name: str) -> list:
    return list(filter(lambda x: plate_name in x['plate_name'], data_list))


def convert_dict_group(data_list: list) -> dict:
    result_dict = {}
    for i in data_list:
        if i['prefecture'] not in result_dict:
            result_dict[i['prefecture']] = [i['plate_name']]
        else:
            result_dict[i['prefecture']].append(i['plate_name'])
    print(result_dict)
    return result_dict


base_data = get_list()

# tokyo = search_prefecture(base_data, '東京')
# print(len(tokyo))
# for i, d in enumerate(tokyo):
#     if len(tokyo) == i + 1:
#         print(f'{d["prefecture"]}: {d["plate_name"]}')
#     else:
#         print(f'{d["prefecture"]}: {d["plate_name"]}', end=', ')
#
# hokkaido = search_prefecture(base_data, '北海道')
# print(len(hokkaido))
# for i, d in enumerate(hokkaido):
#     if len(hokkaido) == i + 1:
#         print(f'{d["prefecture"]}: {d["plate_name"]}')
#     else:
#         print(f'{d["prefecture"]}: {d["plate_name"]}', end=', ')

# convert_dict_group(base_data)
