def get_value(character):
    if character in "123456789":
        return int(character)
    elif character.lower() == 'x' or character == '/':
        return 10
    elif character == '-':
        return 0
    else:
        raise ValueError()


def score(game):
    result = 0
    frame = 1
    in_first_half = True
    
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])

        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i].lower() == "x":
                result += get_value(game[i+1])

                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])

        last = get_value(game[i])

        if not in_first_half:
            frame += 1

        in_first_half = not in_first_half

        if game[i].lower() == 'x':
            in_first_half = True
            frame += 1
            
    return result