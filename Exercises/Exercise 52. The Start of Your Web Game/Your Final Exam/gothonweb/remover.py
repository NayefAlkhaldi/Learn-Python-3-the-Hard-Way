def remove(parsed_path, word_type):     
    for item in parsed_path:
        if item[0] == word_type:
            parsed_path.remove(item)

    return parsed_path