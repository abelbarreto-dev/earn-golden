from re import search


def get_class_name(
        original: str,
) -> str:
    regex = r"<class '.*?\.([A-Za-z]+)'>"

    new_search = search(regex, original)

    if new_search is None:
        raise Exception("the class name wasn't found")

    new_word = new_search.group(1)

    return new_word
