def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = 0
    name = None
    for key, value in a_dictionary.items():
        if best < value:
            best = value
            name = key
    return name
