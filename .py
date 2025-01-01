def sorted_squares(arr):
    # Initialize pointers
    n = len(arr)
    left, right = 0, n - 1
    result = [0] * n
    pos = n - 1  # Start filling from the end of the result array
    
    while left <= right:
        left_sq = arr[left] ** 2
        right_sq = arr[right] ** 2
        
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        
        pos -= 1
    
    return result

# Example usage
input_array = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
output_array = sorted_squares(input_array)
print(output_array)
