def longest_consecutive(numbers: list[int])-> int:
    numbers = set(numbers)
    fin_count = 0
    
    if len(numbers) < 1:
        return 0
    
    for number in numbers:
        if number - 1 in numbers:
            continue
        count = 1
        while number + 1 in numbers:
            number += 1
            count += 1
        fin_count = max(count, fin_count)
        
    return fin_count

# numbers = [100, 4, 200, 1, 3, 2]
# numbers = [1, 2, 3, 4, 5]
# numbers = [10, 30, 20]
# numbers = [1, 1, 2, 2, 3]
# numbers = [9, 1, 4, 7, 3, 2, 6, 5]
# numbers = [-3, -2, -1, 1, 2]
# numbers = [5]
numbers = []
result = longest_consecutive(numbers)
print("Answer:", result)