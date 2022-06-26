def count(limit, incmt, numbers=None):
    # I did that to reset numbers.
    # So, when I call the function again, numbers will disappear.
    if numbers is None:
        numbers = []

    for i in range(limit):
        print(f"At the top i is {i*incmt}")
        numbers.append(i*incmt)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i*incmt}")

        if i*incmt >= limit:
            break

    print("The numbers: ")

    for num in numbers:
        print(num)
    
    return numbers


"""10 is how many times increment to i. 2 is the increment."""
first_call = count(15, 1)
second_call = count(20, 2)
third_call = count(50, 5)

print(first_call, second_call, third_call)