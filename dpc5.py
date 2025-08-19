def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')
    
    # Traverse the array from right to left
    for i in reversed(range(n)):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    # Reverse to maintain original order
    leaders.reverse()
    return leaders
