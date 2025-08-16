def find_missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total - actual_sum
