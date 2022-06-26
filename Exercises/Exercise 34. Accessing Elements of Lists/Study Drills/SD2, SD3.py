def get_integer_name(num):
    numbers_list = ['1st', '2nd', '3rd',
                    '4th', '5th', '6th',
                    '7th', '8th', '9th']

    return str(numbers_list[num])

def get_position(list_of, item, item_name):
    for i, element in enumerate(list_of):
        if element == item:
            print(f"""
            list: {list_of}
            The {element} position is at {i}
            The actual {item_name} position: {get_integer_name(i)}""")


animals = ['bunny', 'cat', 'dog'
           'fish', 'Bird', 'chicken'
           'horse', 'hamester', 'lion']

for animal in animals:
    get_position(animals, animal, 'animal')