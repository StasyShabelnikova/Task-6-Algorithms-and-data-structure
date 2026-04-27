def max_sequence(arr):
    if not arr:
        return 0
    current_len = 1
    max_len = 1
    n = len(arr)
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            current_len = current_len + 1
            max_len = max(current_len, max_len)
        else:
            current_len = 1
    return max_len 