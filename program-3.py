def generate_series_value(n: int):
    result = []
    for i in range(1, n + 1, 2):  
        result.append(i)
    return result


print(generate_series_value(1))  
print(generate_series_value(2))  
print(generate_series_value(3))  
print(generate_series_value(6)) 
