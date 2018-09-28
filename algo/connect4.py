def validate_tocken(token):
    """ Validate token """
    if token != "red" and token != "yellow":
        raise Exception(f"Token value invalid: {token}")


def validate_slot(grid, slot):
    """ Validate slot """
    x, y = slot
    if x > len(grid[0]) or y > len(grid):
        raise Exception(f"Slot values out of range {slot}")


def get_tocken_value(token):
    """Get the token value, 1 for RED and 2 for YELLOW"""
    return 1 if token == "red" else 2


def move(grid, token, slot):
    validate_tocken(token)
    validate_slot(grid, slot)
    # update grid value
    x, y = slot
    grid[x][y] = get_tocken_value(token)


def check_last_move(grid, token, slot):
    validate_tocken(token)
    validate_slot(grid, slot)

    token_value = get_tocken_value(token)

    x, y = slot
    # check the column
    if all([token_value == grid[i][y] for i in range(len(grid))]):
        return True

    # check the row
    if all([token_value == grid[x][j] for j in range(len(grid[0]))]):
        return True

    # check diagonal
    # TODO

    return False


def main():
    grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    token = "yellow"
    slot = [0, 0]
    move(grid, token, slot)
    if check_last_move(grid, token, slot) is True:
        print(f"The {token} player has won.")
    else:
        print("The game is not over.")


if __name__ == "__main__":
    main()
