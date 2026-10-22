def majority_element(numbers: list[int]) -> int | None:
    if not numbers:
        return None
    
    candidate = None
    count = 0
    
    for num in numbers:
        if count == 0:
            candidate = num
            
        count += (1 if num == candidate else -1)
        
    if numbers.count(candidate) > len(numbers) // 2:
        return candidate
        
    return None