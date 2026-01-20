def multiply_by_2(a_dictionary):
    keys_dic = list(a_dictionary)
    dic_two = {keys: a_dictionary[keys]*2 for keys in keys_dic}
    return dic_two
