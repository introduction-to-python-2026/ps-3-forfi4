def move(my_list, direction):
    try:
        current_index = my_list.index(1)
    except ValueError:
        return my_list

    list_length = len(my_list)

    if direction == 'right':
        if current_index < list_length - 1:
            # Move the pig right
            my_list[current_index] = 0
            my_list[current_index + 1] = 1
    elif direction == 'left':
        if current_index > 0:
            # Move the pig left
            my_list[current_index] = 0
            my_list[current_index - 1] = 1
            
    return my_list
print(f"move([0, 0, 0, 1, 0], 'right'): {move([0, 0, 0, 1, 0], 'right')}")
print(f"move([0, 1, 0, 0, 0], 'left'):  {move([0, 1, 0, 0, 0], 'left')}")

print(f"move([1, 0, 0, 0, 0], 'left'):  {move([1, 0, 0, 0, 0], 'left')}")
print(f"move([0, 0, 0, 0, 1], 'right'): {move([0, 0, 0, 0, 1], 'right')}")
