def runner():

    light_x, light_y, initial_tx, initial_ty = 36, 17, 0, 0
    i = 0
# game loop
    while i < 30:
    # remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        delta_x = initial_tx - light_x
        delta_y = initial_ty - light_y
        answer = ""

    # A single line providing the move to be made: N NE E SE S SW W or NW
        if delta_y < 0:
            answer += "S"
            initial_ty += 1
        elif delta_y > 0:
            answer += "N"
            initial_ty -= 1
        if delta_x < 0:
            answer += "E"
            initial_tx += 1
        elif delta_x > 0:
            answer += "W"
            initial_tx -= 1
        print(answer)
        print(initial_tx, initial_ty)
        i += 1



if __name__ == "__main__":
    runner()
