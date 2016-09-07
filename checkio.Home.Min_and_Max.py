def min(*args, **kwargs):
    key = kwargs.get("key", None)
    data = args if len(args) > 1 else list(args[0])
    if key:
        minimal = data[0]
        for x in data[1:]:
            if key(x) < key(minimal):
                minimal = x
    else:
        minimal = data[0]
        for x in data[1:]:
            if x < minimal:
                minimal = x

    return minimal

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    data = args if len(args) > 1 else list(args[0])
    if key:
        maximum = data[0]
        for x in data[1:]:
            if key(x) > key(maximum):
                maximum = x
    else:
        maximum = data[0]
        for x in data[1:]:
            if x > maximum:
                maximum = x

    return maximum

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    min(abs(i) for i in range(-10, 10))
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
