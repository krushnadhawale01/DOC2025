def dutch_national_flag_sort(nums):
    start = 0
    current = 0
    end = len(nums) - 1

    while current <= end:
        value = nums[current]
        if value == 0:
            nums[start], nums[current] = nums[current], nums[start]
            start += 1
            current += 1
        elif value == 1:
            current += 1
        else:  # value == 2
            nums[current], nums[end] = nums[end], nums[current]
            end -= 1
    return nums
