from lark import Token as token


def push_array(arr, item):
    arr.append(item)
    return arr


def lexeme(item):
    if isinstance(item, token):
        return item.value
    elif isinstance(item, str):
        return item
    else:
        raise Exception("Unknown item type")
