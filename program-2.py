def generate_series_terms(n: int):
    result = []
    for i in range(n):
        result.append(2 * i + 1) 
    return result 
print(generate_series_terms(1)) 
print(generate_series_terms(2))  
print(generate_series_terms(4))  
