def check_str(x, _for=""):
    if not isinstance(x, str):
        raise TypeError("Expected string, but got {}. {}".format(str(type(x)), _for))
    return True


def number_to_position(num: int):
    assert num > 0, "use strictly positive numbers in number_to_position()"
    return (
        {1: "{}st", 2: "{}nd", 3: "{}rd"}.get(
            num if (num < 20) else (num % 10), "{}th"
        )
    ).format(num)
