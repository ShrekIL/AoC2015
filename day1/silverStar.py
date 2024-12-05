def calculate_floor(instructions):
    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor

if __name__ == "__main__":
    with open('day1/input.txt', 'r') as file:
        instructions = file.read().strip()
    result = calculate_floor(instructions)
    print(f"The resulting floor is: {result}")
