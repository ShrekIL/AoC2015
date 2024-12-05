def find_basement_position(instructions):
    floor = 0
    for position, char in enumerate(instructions, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return position
    return None

if __name__ == "__main__":
    with open('day1/input.txt', 'r') as file:
        instructions = file.read().strip()
    
    basement_position = find_basement_position(instructions)
    if basement_position:
        print(f"The position of the first character that causes Santa to enter the basement is: {basement_position}")
    else:
        print("Santa never enters the basement.")
