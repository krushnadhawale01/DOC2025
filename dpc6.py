def find_zero_sum_subarrays(arr):
    prefix_sum = 0
    sum_indices = {0: [-1]}  # Handle case when subarray starts at index 0
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum in sum_indices:
            for start_index in sum_indices[prefix_sum]:
                result.append((start_index + 1, i))

        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = []
        sum_indices[prefix_sum].append(i)

    return result
