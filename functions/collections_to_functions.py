import random
import string


def generate_dicts() -> list:
    """
    This function produces list of dicts of variable length with key=str and value=int.
    :return: List of dicts.
    """
    dict_list = [{} for elem in range(2, 10)]
    for elem in dict_list:
        while len(elem) != 3:
            elem[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
    return dict_list


def get_all_the_keys(dict_list: list) -> list:
    """
    This function is used for collecting all the keys into one list
    :param dict_list: Result of generate_dicts() function execution
    :return: List of all the keys which are present in all the dicts.
    """
    list_of_all_keys = []
    for elem in dict_list:
        list_of_all_keys += elem.keys()
    return list_of_all_keys


def get_the_unique_key_list(dict_list: list) -> list:
    """
    This function creates list of unique keys only for future iterations.
    :param dict_list: Result of generate_dicts() function execution
    :return: List of unique ordered keys
    """
    list_of_all_keys = get_all_the_keys(dict_list)
    return sorted(list(set(list_of_all_keys)))


def merge_into_one_dict(dict_list: list, list_of_all_keys: list, ordered_unique_keys: list) -> dict:
    """
    This function merges all the dicts from list into one dict.
    :param dict_list: Result of generate_dicts() function execution
    :param list_of_all_keys: Result of get_all_the_keys() function execution
    :param ordered_unique_keys: Result of get_the_unique_key_list() function execution
    :return: One dict which contains single letter if key was presented once or key + index number from dict_list
    to observe from which dict we have max value and max value (in case if key presents in several dicts)
    """
    final_dict = {}
    for elem in ordered_unique_keys:
        if list_of_all_keys.count(elem) > 1:
            max_value = 0
            index = 0
            for one_dict in dict_list:
                if elem in one_dict:
                    if max_value < one_dict.get(elem):
                        max_value = one_dict.get(elem)
                        index = dict_list.index(one_dict)
            final_dict[f'{elem}_{index}'] = max_value
        else:
            for one_dict in dict_list:
                if elem in one_dict:
                    final_dict[elem] = one_dict.get(elem)
                    break
    return final_dict

# calling all the functions. Used walrus operator to reduce strings of code by assigning and execution at the same time.
# For the first 3 calls since I'll use these variables in the last call
print(dicts_created := generate_dicts())
print(key_list := get_all_the_keys(dicts_created))
print(unique_keys_list := get_the_unique_key_list(dicts_created))
print(merge_into_one_dict(dicts_created, key_list, unique_keys_list))
