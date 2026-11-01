def linear_search(arr, target):
    """
    Performs a linear search on a list.
    Returns the index of the target if found, otherwise returns -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index  # Target found, return current index
            
    return -1  # Target not found after checking the whole list


# Example Usage:
numbers = [10, 23, 45, 70, 11, 15]
target_value = 70

result = linear_search(numbers, target_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")
