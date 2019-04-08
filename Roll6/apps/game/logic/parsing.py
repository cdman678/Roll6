def stringToList(string):
    out = []
    if isinstance(string, str):
        out = string.split(',')
    return out
