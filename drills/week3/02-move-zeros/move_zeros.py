def move_zeros(numbers: list[int]) -> list:
    initial = 0
    for number in range(len(numbers)):
        if numbers[number] != 0:
            numbers[initial], numbers[number] = numbers[number], numbers[initial]
            initial += 1
            
    return numbers

# numbers = [0, 1, 0, 3, 12]
# print(move_zeros(numbers))