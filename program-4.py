def count_multiples(nums):
    divisors = [1,2,3,4,5,6,7,8,9]
    result = {d: 0 for d in divisors}
    
    for num in nums:
        for d in divisors:
            if num % d == 0:
                result[d] += 1
    return result
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(nums))
