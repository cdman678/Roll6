def string_to_list(string):
    """
    :param string: The string to split, should be a comma separated list
    :return: the list of strings
    """
    out = []
    if isinstance(string, str):
        out = string.split(',')
    return out
