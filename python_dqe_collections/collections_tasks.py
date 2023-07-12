import random
import string

# creating a list of dicts of variable length using list comprehension.
dict_list = [{} for elem in range(2, 10)]

# filling dicts with keys and values using string and random. Condition on length of each dict to have loop interruption.
# in case we need variable quantity of keys in each dict we can use construction while len(elem) != randint(1, len(string.ascii_lowercase)
for elem in dict_list:
    while len(elem) != 3:
        elem[random.choice(string.ascii_lowercase)] = random.randint(0, 100)

# creating variable to contain all the keys in the future.
list_of_all_keys = []

# merging keys of all dicts with early created variable using concatenation.
for elem in dict_list:
    list_of_all_keys += elem.keys()

# creating an ordered list of unique keys using types casting from set to list.
ordered_unique_keys = sorted(list(set(list_of_all_keys)))

# creating a variable to contain final dict with unique values.
final_dict = {}

# iterating with unique key over our existing list to paste the values for our final dict.
for elem in ordered_unique_keys:
# validation if our key is used more that in one dict.
    if list_of_all_keys.count(elem) > 1:
# created variables to contain values of max value and index of dict.
        max_value = 0
        index = 0
# iterating over our original dict list to validate against our key.
        for one_dict in dict_list:
# validation of key presence inside one dict.
            if elem in one_dict:
# check on max value. If value is bigger - we are assigning it to max value and assigning index.
                if max_value < one_dict.get(elem):
                    max_value = one_dict.get(elem)
                    index = dict_list.index(one_dict)
# assigning value to the key which is formatted using f string.
        final_dict[f'{elem}_{index}'] = max_value
# making max_value and index back to 0 to keep iteration logic properly.
        max_value = 0
        index = 0
# else condition which handles scenarios for cases when key is used only once.
    else:
        for one_dict in dict_list:
            if elem in one_dict:
                final_dict[elem] = one_dict.get(elem)
                break

# simply printing final dict to make solution demonstrative
print(final_dict)
