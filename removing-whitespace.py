def remove_whitespace(s):
    new_str = ""
    for char in s:
        if char != " ":
            new_str += char
    return new_str
