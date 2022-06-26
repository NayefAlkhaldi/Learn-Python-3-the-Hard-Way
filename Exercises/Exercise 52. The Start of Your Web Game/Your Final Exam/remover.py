class RemoveError(Exception):
    pass

def remove(parsed_path, word_type):
    for item in parsed_path:
        if item[0] == word_type:
            parsed_path.remove(item)

    if parsed_path == []:
        raise RemoveError(
            f"Empty list after removing."
        )

    return parsed_path