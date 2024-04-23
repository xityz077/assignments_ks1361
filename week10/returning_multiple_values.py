def get_extremes(number_list):
    min_val = min(number_list)
    max_val = max(number_list)
    return (min_val, max_val) # ( ) not required

# Call the get_extremes function
numbers = [5, 3, 2, 7, 2, 5]
low, high = get_extremes(numbers)
print(low)
print(high)
