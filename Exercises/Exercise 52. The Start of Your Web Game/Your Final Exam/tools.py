start_time = None
end_time = None

def calculate_time(total_time):
    seconds = 0
    minutes = 0
    hours = 0

    while True:
        if total_time >= 60:
            total_time -= 60
            minutes += 1

            if minutes >= 60:
                hours += 1
                minutes -= 60

        else:
            seconds += total_time
            if len(str(hours)) == 1:
                hours = f"0{hours}"

            if len(str(minutes)) == 1:
                minutes = f"0{minutes}"

            if len(str(seconds)) == 1:
                minutes = f"0{seconds}"
            break

    return f"{hours}h {minutes}m {seconds}s"

def get_real_time(time):

    time = time.replace(' ', '')

    find_place = {
        'h1': 0,
        'h2': 1,
        'm1': 3,
        'm2': 4,
        's1': 6,
        's2': 7,
    }

    calculate = {
        'h': 3600,
        'm': 60,
        's': 1,
    }

    seconds = 0
    for letter in time:
        if letter in calculate.keys():
            first_digit = str(time)[find_place[f'{letter}1']]
            second_digit = str(time)[find_place[f'{letter}2']]

            number = str(first_digit + second_digit)
            result = int(number) * calculate[letter]
            seconds += result

    return seconds