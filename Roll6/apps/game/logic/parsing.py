def string_to_list(string):
    """
    :param string: The string to split, should be a comma separated list
    :return: the list of strings
    """
    out = []
    if isinstance(string, str):
        out = string.split(',')
    return out


def list_to_string(array):
    out = ""
    for string in array:
        if out:
            out += ','
        out += string
    return out
