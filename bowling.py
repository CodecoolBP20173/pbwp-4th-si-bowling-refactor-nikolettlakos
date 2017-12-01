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
    
    for x in range(len(game)):
        if game[x] == '/':
            result += 10 - last
        else:
            result += get_value(game[x])

        if frame < 10 and get_value(game[x]) == 10:
            if game[x] == '/':
                result += get_value(game[x+1])
            elif game[x].lower() == "x":
                result += get_value(game[x+1])

                if game[x+2] == '/':
                    result += 10 - get_value(game[x+1])
                else:
                    result += get_value(game[x+2])

        last = get_value(game[x])

        if not in_first_half:
            frame += 1

        in_first_half = not in_first_half

        if game[x].lower() == 'x':
            in_first_half = True
            frame += 1
            
    return result