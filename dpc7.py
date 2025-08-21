def trap(height):
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    max_left, max_right = height[left], height[right]
    trapped = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            max_left = max(max_left, height[left])
            trapped += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            trapped += max_right - height[right]

    return trapped
