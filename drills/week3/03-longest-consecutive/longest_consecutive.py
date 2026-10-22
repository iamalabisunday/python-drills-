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

numbers = []
result = longest_consecutive(numbers)
print("Answer:", result)