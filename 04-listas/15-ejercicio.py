# Parsear diccionarios con una libreria
from pprint import pprint


def delete_white_spaces(str: str):
    splitted_string = [*str.strip().replace(' ', '')]
    return splitted_string


def count_repeated_words(str: str):
    res = {}
    for word in str.strip().replace(' ', ""):
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res


def order_dictionary_to_tuple(dictionary: dict):
    res = sorted(
        dictionary.items(),
        key=lambda elm: elm[1],
        reverse=True
    )
    return res


def order_tuple_desc(tupla: tuple):
    new_list = list(tupla)
    new_list.sort(key=lambda element: element[1], reverse=True)
    if not new_list:
        return tupla
    max_value = new_list[0]
    filtered_values = list(
        filter(lambda elem: elem[1] == max_value[1], new_list))
    return tuple(filtered_values)


def repeated_chars(str: str, no=4):
    values_array = count_repeated_words(str.upper())
    count_repeated_chars = list(
        filter(lambda elem: elem[1] >= no, values_array.items()))
    res = ''
    for word in count_repeated_chars:
        res += f'- {word[0]} \n'
    return res
